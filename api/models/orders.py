from sqlalchemy import Column, DateTime, DECIMAL, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    promotion_id = Column(Integer, ForeignKey("promotions.id"), nullable=True)
    customer_name = Column(String(120), nullable=False)
    order_date = Column(DateTime, nullable=False, server_default=func.now())
    tracking_number = Column(String(64), unique=True, index=True, nullable=False)
    status = Column(String(40), nullable=False, server_default="pending")
    order_type = Column(String(40), nullable=False)  # e.g., "takeout" or "delivery"
    total_price = Column(DECIMAL(10, 2), nullable=False, server_default="0.00")
    description = Column(String(300), nullable=True)

    customer = relationship("Customer", back_populates="orders")
    promotion = relationship("Promotion", back_populates="orders")
    order_details = relationship("OrderDetail", back_populates="order", cascade="all, delete-orphan")
    payment = relationship("Payment", back_populates="order", uselist=False)