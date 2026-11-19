from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict

class PaymentBase(BaseModel):
    order_id: int
    payment_type: str
    card_last_four: Optional[str] = None
    transaction_status: str
    amount: Decimal

class PaymentCreate(PaymentBase):
    pass

class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    card_last_four: Optional[str] = None
    transaction_status: Optional[str] = None
    amount: Optional[Decimal] = None

class Payment(PaymentBase):
    id: int
    payment_date: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)