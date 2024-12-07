from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PromotionBase(BaseModel):
    code: str
    expiration_date: datetime

class PromotionCreate(PromotionBase):
    pass  # No additional fields for creation

class PromotionUpdate(BaseModel):
    code: Optional[str] = None
    expiration_date: Optional[datetime] = None

class Promotion(PromotionBase):
    id: int

    class Config:
        orm_mode = True