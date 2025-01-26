# ./models/Token.py

from sqlmodel import Field, Relationship

from ..db.Base import BaseModel
from .User import User

class Notification(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id")  # Foreign key to users table
    message: str  # Notification message (e.g., "Password reset email sent")
    is_read: bool = Field(default=False)  # Whether the notification has been read

    # Relationships
    user: "User" = Relationship(back_populates="notifications")
