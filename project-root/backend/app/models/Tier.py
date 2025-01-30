# models/tier.py

from sqlmodel import Field, Relationship
from typing import List, Optional
from datetime import datetime

from .Base import BaseModel

class Tier(BaseModel, table=True):
    name: str  
    label: Optional[str] = None  
    description: Optional[str] = None 

    # Relationships
    prices: List["TierPrice"] = Relationship(back_populates="tier")
   
class TierPrice(BaseModel, table=True):
    tier_id: int = Field(foreign_key="tier.id") 
    name: str  
    label: Optional[str] = None  
    description: Optional[str] = None 
    currency: str = Field(default="usd") 
    stripe_product_id: str 
    stripe_price_id: str 
    price: float                                                    
    expires_at: Optional[datetime] = None                          

    # Relationships
    tier: "Tier" = Relationship(back_populates="prices")