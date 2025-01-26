# ./models.Payment.py

from sqlmodel import Field, Relationship

from ..db.Base import BaseModel
from .User import User


class PaymentHistory(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id")  # Foreign key to users table
    amount: float  # Payment amount
    currency: str = Field(default="usd")  # Payment currency (e.g., "usd")
    description: str  # Description of the payment (e.g., "Subscription A")
    stripe_payment_intent_id: str  # Stripe payment intent ID
    status: str  # Payment status (e.g., "succeeded", "failed")

    # Relationships
    user: "User" = Relationship(back_populates="payment_history")

