# ./models/Token.py

from sqlmodel import Field, Relationship
from typing import Optional
from datetime import datetime

from .Base import BaseModel
from .User import User

class TokenBalance(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)  # Foreign key to users table
    balance: int = Field(default=0)  # Current token balance
    last_credited: Optional[datetime] = None  # Last time tokens were credited

    # Relationships
    user: "User" = Relationship(back_populates="token_balance")
