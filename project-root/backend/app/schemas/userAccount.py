# schemas/userAccount.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# UserPayment
class UserPaymentBase(BaseModel):
    stripe_invoice_id: str
    amount: float
    currency: str = "usd"
    status: str
    payment_date: datetime

class UserPaymentCreate(UserPaymentBase):
    user_id: int

class UserPaymentRead(UserPaymentBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# UserSubscription
class UserSubscriptionBase(BaseModel):
    stripe_subscription_id: str
    status: str
    status_date: datetime
    end_date: Optional[datetime] = None
    renewal_date: Optional[datetime] = None
    cancel_at_period_end: bool = False

class UserSubscriptionCreate(UserSubscriptionBase):
    user_id: int
    tier_id: int

class UserSubscriptionRead(UserSubscriptionBase):
    id: int
    user_id: int
    tier_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# UserTier
class UserTierBase(BaseModel):
    start_date: datetime
    expiration_date: Optional[datetime] = None
    price_paid: float
    currency: str = "usd"

class UserTierCreate(UserTierBase):
    user_id: int
    tier_id: int

class UserTierRead(UserTierBase):
    id: int
    user_id: int
    tier_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# UserCreditBalance
class UserCreditBalanceBase(BaseModel):
    balance: int = 0
    last_credited: Optional[datetime] = None

class UserCreditBalanceCreate(UserCreditBalanceBase):
    user_id: int

class UserCreditBalanceRead(UserCreditBalanceBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True