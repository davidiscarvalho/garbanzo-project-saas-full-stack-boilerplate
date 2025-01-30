# schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# Base schemas
class UserBase(BaseModel):
    email: EmailStr
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False

# Request schemas
class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None

# Response schemas
class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    created_by: str
    updated_by: str

    class Config:
        from_attributes = True  # Enable ORM mode for SQLModel


# Role
class RoleBase(BaseModel):
    name: str
    description: Optional[str] = None

class RoleCreate(RoleBase):
    pass

class RoleRead(RoleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Permission
class PermissionBase(BaseModel):
    name: str
    description: Optional[str] = None

class PermissionCreate(PermissionBase):
    pass

class PermissionRead(PermissionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# RolePermission
class RolePermissionBase(BaseModel):
    role_id: int
    permission_id: int

class RolePermissionCreate(RolePermissionBase):
    pass

class RolePermissionRead(RolePermissionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# UserRole
class UserRoleBase(BaseModel):
    user_id: int
    role_id: int

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleRead(UserRoleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True