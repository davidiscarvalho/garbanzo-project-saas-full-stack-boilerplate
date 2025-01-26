# db/Base.py

from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional

class BaseModel(SQLModel):
    """
    Base model for all database tables.
    Includes common fields like id, created_at, updated_at, created_by, and updated_by.
    """

    # Primary key for the table
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow,nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow,nullable=False)
    created_by: str = Field(default="system",nullable=False)
    updated_by: str = Field(default="system",nullable=False)