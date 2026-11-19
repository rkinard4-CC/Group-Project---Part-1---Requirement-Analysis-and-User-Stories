from sqlalchemy import Column, DateTime, DECIMAL, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, pimary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"), unique=True, nullable=False)
    payment_type =Column(String(50), nullable=False)
    card_last_four = Column(String(4), nullable=False)
    transaction_status = Column(String(50), nullable=False)
    amount = Column(DECIMAL(20, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False, server_default=func.now())

    order = relationship("Order", back_populates="payment")