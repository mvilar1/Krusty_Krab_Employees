from pydantic import BaseModel, condecimal
from typing import Optional

class MenuItemBase(BaseModel):
    name: str
    price: condecimal(max_digits=10, decimal_places=2)
    calories: Optional[int]
    category: Optional[str]

class MenuItemCreate(MenuItemBase):
    pass  # No additional fields for creation

class MenuItemUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[condecimal(max_digits=10, decimal_places=2)] = None
    calories: Optional[int] = None
    category: Optional[str] = None

class MenuItem(MenuItemBase):
    id: int

    class Config:
        orm_mode = True