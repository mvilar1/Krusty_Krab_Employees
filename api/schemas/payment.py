from pydantic import BaseModel, condecimal
from typing import Optional

class PaymentBase(BaseModel):
    payment_type: str
    transaction_status: str
    card_information: Optional[str]  # Mask or encrypt in production

class PaymentCreate(PaymentBase):
    pass  # No additional fields for creation

class PaymentUpdate(BaseModel):
    payment_type: Optional[str] = None
    transaction_status: Optional[str] = None
    card_information: Optional[str] = None

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True