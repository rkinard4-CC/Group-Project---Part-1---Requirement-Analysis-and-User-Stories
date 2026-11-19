from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    rating = Column(Integer, nullable=False)
    review_text = Column(String(500), nullable=True)
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    customer = relationship("Customer", back_populates="reviews")
    menu_item = relationship("MenuItem", back_populates="reviews")