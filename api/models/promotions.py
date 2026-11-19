from sqlalchemy import Boolean, Column, DateTime, DECIMAL, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Promotion(Base):
    __tablename__ = "promotions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    code = Column(String(50), unique=True, index=True, nullable=False)
    description = Column(String(225), nullable=True)
    discount_percent = Column(DECIMAL(5, 2), nullable=False, server_default="0.00")
    expiration_date = Column(DateTime, nullable=True)
    is_active = Column(Boolean, nullable=False, server_default="1")

    orders = relationship("Order", back_populates="promotion")
