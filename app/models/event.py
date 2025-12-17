from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from .base import Base

class Event(Base):
    __tablename__ = "events"

    event_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    product_id = Column(Integer, ForeignKey("products.product_id"))
    event_type = Column(String)
    timestamp = Column(DateTime)