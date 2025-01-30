# models/UserAccount.py

from sqlmodel import Field, Relationship
from datetime import datetime
from typing import Optional

from .Base import BaseModel
from .User import User
from .Tier import Tier

class UserPayment(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id") 
    stripe_invoice_id: str = Field(index=True)
    amount: float 
    currency: str = Field(default="usd") 
    status: str 
    payment_date: datetime = Field(default_factory=datetime.utcnow) 
    # Relationships
    user: "User" = Relationship(back_populates="payments")


class UserSubscription(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id")  
    tier_id: int = Field(foreign_key="tier.id")  
    stripe_subscription_id: str = Field(index=True) 
    status: str  
    status_date: datetime = Field(default_factory=datetime.utcnow)  
    end_date: Optional[datetime] = None 
    renewal_date: Optional[datetime] = None 
    cancel_at_period_end: bool = Field(default=False)  

    # Relationships
    user: "User" = Relationship(back_populates="subscriptions")
    tier: "Tier" = Relationship(back_populates="subscriptions")


class UserTier(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id")  
    tier_id: int = Field(foreign_key="tier.id") 
    start_date: datetime = Field(default_factory=datetime.utcnow) 
    expiration_date: Optional[datetime] = None  
    price_paid: float  
    currency: str = Field(default="usd")  

    # Relationships
    user: "User" = Relationship(back_populates="tiers")
    tier: "Tier" = Relationship(back_populates="user_tiers")

class UserCreditBalance(BaseModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)  # Foreign key to users table
    balance: int = Field(default=0)  # Current Credit balance
    last_credited: Optional[datetime] = None  # Last time tokens were credited

    # Relationships
    user: "User" = Relationship(back_populates="credit_balance")