# ./models/Subscription.py

from sqlmodel import Field, Relationship

from ..db.Base import BaseModel
from .User import User

class Subscription(BaseModel, table=True):
    """
    Subscription model representing a subscription in the database.
    Inherits from BaseModel to include common fields.
    """
    user_id: int = Field(foreign_key="user.id")  # Foreign key to users table
    name: str  # Subscription name (e.g., "Subscription A")
    price: float  # Subscription price
    currency: str = Field(default="usd")  # Subscription currency (e.g., "usd")
    interval: str  # Subscription interval (e.g., "month", "year")
    stripe_subscription_id: str  # Stripe subscription ID
    status: str  # Subscription status (e.g., "active", "canceled")

    # Relationships
    user: "User" = Relationship(back_populates="subscriptions")