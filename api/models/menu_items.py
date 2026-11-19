from sqlalchemy import Column, DECIMAL, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(120), unique=True, index=True, nullable=False)
    description = Column(String(120), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False, server_default="0.00")
    calories = Column(Integer, nullable=True)
    category = Column(String(80), nullable=True)

    recipes = relationship("Recipe", back_populates="menu_item", cascade="all, delete-orphan")
    order_details = relationship("OrderDetail", back_populates="menu_item")
    reviews = relationship("Review", back_populates="menu_item", cascade="all, delete-orphan")