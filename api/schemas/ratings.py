from pydantic import BaseModel, conint
from typing import Optional

class RatingBase(BaseModel):
    review_text: Optional[str]
    score: conint(ge=1, le=5)  # Ensures score is between 1 and 5

class RatingCreate(RatingBase):
    customer_id: int
    menu_item_id: int

class RatingUpdate(BaseModel):
    review_text: Optional[str] = None
    score: Optional[conint(ge=1, le=5)] = None

class Rating(RatingBase):
    id: int
    customer_id: int
    menu_item_id: int

    class Config:
        orm_mode = True