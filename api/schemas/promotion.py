from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict

class PromotionBase(BaseModel):
    code: str
    description: Optional[str] = None
    discount_percent: Decimal
    expiration_date: Optional[datetime] = None
    is_active: bool = True

class PromotionCreate(PromotionBase):
    pass

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    description: Optional[str] = None
    discount_percent: Optional[Decimal] = None
    expiration_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class Promotion(PromotionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)