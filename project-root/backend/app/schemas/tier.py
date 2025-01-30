# schemas/tier.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Tier
class TierBase(BaseModel):
    name: str
    label: Optional[str] = None
    description: Optional[str] = None

class TierCreate(TierBase):
    pass

class TierRead(TierBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# TierPrice
class TierPriceBase(BaseModel):
    name: str
    label: Optional[str] = None
    description: Optional[str] = None
    currency: str = "usd"
    stripe_product_id: str
    stripe_price_id: str
    price: float
    expires_at: Optional[datetime] = None

class TierPriceCreate(TierPriceBase):
    tier_id: int

class TierPriceRead(TierPriceBase):
    id: int
    tier_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
