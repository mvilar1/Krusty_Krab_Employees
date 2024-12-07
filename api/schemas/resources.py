from pydantic import BaseModel
from typing import Optional

class ResourceBase(BaseModel):
    ingredient_name: str
    amount: float
    unit: str

class ResourceCreate(ResourceBase):
    pass  # No additional fields for creation

class ResourceUpdate(BaseModel):
    ingredient_name: Optional[str] = None
    amount: Optional[float] = None
    unit: Optional[str] = None

class Resource(ResourceBase):
    id: int

    class Config:
        orm_mode = True
