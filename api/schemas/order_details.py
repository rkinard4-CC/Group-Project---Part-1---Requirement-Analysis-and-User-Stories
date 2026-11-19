from typing import Optional
from pydantic import BaseModel, ConfigDict
from .menu_items import MenuItem


class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    menu_item_id: int


class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    menu_item_id: int
    menu_item: Optional[MenuItem] = None

    model_config = ConfigDict(from_attributes=True)