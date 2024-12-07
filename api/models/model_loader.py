from ..dependencies.database import Base, engine
from ..models.customers import Customer
from ..models.ratings import Rating
from ..models.payment import Payment
from ..models.orders import Order
from ..models.menu_items import MenuItem
from ..models.resources import Resource
from ..models.promotions import Promotion

# Create tables based on the updated models
Base.metadata.create_all(bind=engine)
