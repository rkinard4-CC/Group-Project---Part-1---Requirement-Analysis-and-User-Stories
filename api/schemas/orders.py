from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail



class OrderBase(BaseModel):
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None
    customer_name: str
    order_type: str
    description: Optional[str] = None


class OrderCreate(OrderBase):
    pass


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    promotion_id: Optional[int] = None
    customer_name: Optional[str] = None
    status: Optional[str] = None
    order_type: Optional[str] = None
    total_price: Optional[Decimal] = None
    description: Optional[str] = None


class Order(OrderBase):
    id: int
    order_date: Optional[datetime] = None
    tracking_number: str
    status: str
    total_price: Optional[Decimal] = None
    order_details: Optional[list[OrderDetail]] = None

    class ConfigDict:
        from_attributes = True
