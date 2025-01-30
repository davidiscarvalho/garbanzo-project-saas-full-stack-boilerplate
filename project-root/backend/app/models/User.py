# ./models/User.py

from sqlmodel import Field, Relationship
from typing import Optional, List

from .Base import BaseModel

class User(BaseModel, table=True):
    """
    User model representing a user in the database.
    Inherits from BaseModel to include common fields.
    """
    email: str = Field(unique=True, index=True)
    hashed_password: str = Field(nullable=False)
    full_name: Optional[str] = None
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)

    # Verify password
    def verify_password(self, password: str) -> bool:
        from ..core.auth import verify_password  # Import the verify_password function
        return verify_password(password, self.hashed_password)

class Role(BaseModel, table=True):
    """
    Role model (for role-based access control)
    Inherits from BaseModel to include common fields.
    """
    name: str = Field(unique=True, index=True)  # Role name (e.g., "admin", "user")
    description: Optional[str] = None

class UserRole(BaseModel, table=True):
    """
    UserRole model (many-to-many between User and Role)
    Inherits from BaseModel to include common fields.
    """
    user_id: int = Field(foreign_key="user.id")
    role_id: int = Field(foreign_key="role.id")

    # Relationships
    user: "User" = Relationship(back_populates="roles")
    role: "Role" = Relationship(back_populates="users")

class Permission(BaseModel, table=True):
    """
    Permission model (for role-based access control)
    Inherits from BaseModel to include common fields.
    """
    name: str = Field(unique=True, index=True)
    description: Optional[str] = None


class RolePermission(BaseModel, table=True):
    """
    RolePermission model (many-to-many between Role and Permission)
    Inherits from BaseModel to include common fields.
    """
    role_id: int = Field(foreign_key="role.id")
    permission_id: int = Field(foreign_key="permission.id")

    # Relationships
    role: "Role" = Relationship(back_populates="permissions")
    permission: "Permission" = Relationship(back_populates="roles")