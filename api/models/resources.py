from sqlalchemy import Column, Integer, String, DECIMAL
from ..dependencies.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    unit = Column(String(50), nullable=False)