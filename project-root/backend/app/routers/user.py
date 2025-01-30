# routers/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List

from db.session import get_session
from models.User import User
from schemas.user import UserCreate, UserRead, UserUpdate, UserRoleCreate, UserRoleRead

from core.auth import get_current_user, check_permission

router = APIRouter(prefix="/users", tags=["Users"])

# Create User
@router.post("/", response_model=UserRead)
def create_user(*, session: Session = Depends(get_session), user: UserCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    db_user = User.from_orm(user)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# Read User
@router.get("/{user_id}", response_model=UserRead)
def read_user(*, session: Session = Depends(get_session), user_id: int, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update User
@router.put("/{user_id}", response_model=UserRead)
def update_user(*, session: Session = Depends(get_session), user_id: int, user: UserUpdate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "update")
    db_user = session.get(User, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

# Delete User
@router.delete("/{user_id}")
def delete_user(*, session: Session = Depends(get_session), user_id: int, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "delete")
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"ok": True}

# List Users
@router.get("/", response_model=List[UserRead])
def list_users(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    users = session.exec(select(User)).all()
    return users

# UserRole
@router.post("/{user_id}/roles/", response_model=UserRoleRead)
def create_user_role(*, session: Session = Depends(get_session), user_role: UserRoleCreate, current_user: User = Depends(get_current_user)):
    check_permission(current_user, "create")
    pass
    return 

@router.get("/{user_id}/roles/", response_model=List[UserRoleRead])
def list_user_roles(*, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    check_permission(current_user, "read")
    pass
    return 