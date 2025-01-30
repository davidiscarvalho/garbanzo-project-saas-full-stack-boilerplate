# ./core/auth.py

from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt

from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session

from db.session import get_session
from core.config import settings
from models.User import User

# JWT Configuration
SECRET_KEY = settings.SECRET_KEY_JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Hash password
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Create JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode JWT token
def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

# Get current user from token
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    email: str = payload.get("sub")
    if email is None:
        raise credentials_exception
    # user = session.exec(select(User).where(User.email == email)).first()
    # if user is None:
    #     raise credentials_exception
    # return user

# Get current active user
async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Helper function to check if the user has a specific permission
def has_permission(user: User, permission_name: str) -> bool:
    """
    Check if the user has the required permission.
    Returns True if the user has the permission, otherwise False.
    """
    for role in user.roles:
        for permission in role.permissions:
            if permission.name == permission_name:
                return True
    return False

# Check if the user has a specific permission
def check_permission(user: User, permission_name: str):
    """
    Check if the user has the required permission.
    Raises HTTPException with 403 status if the user doesn't have the permission.
    """
    if not has_permission(user, permission_name):
        raise HTTPException(status_code=403, detail="Permission denied")

