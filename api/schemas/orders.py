from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .menu_items import MenuItem

class OrderBase(BaseModel):
    order_date: datetime
    tracking_number: str
    order_status: str
    total_price: float

class OrderCreate(OrderBase):
    customer_id: int

class OrderUpdate(BaseModel):
    order_date: Optional[datetime] = None
    tracking_number: Optional[str] = None
    order_status: Optional[str] = None
    total_price: Optional[float] = None

class Order(OrderBase):
    id: int
    customer_id: int
    menu_items: List[MenuItem] = []  # Related items

    class Config:
        orm_mode = True
