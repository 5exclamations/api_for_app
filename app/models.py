from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship
from .database1 import Base


class Market(Base):
    __tablename__ = "markets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    logo_url = Column(String, nullable=False)

    products = relationship("Product", back_populates="market")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    icon = Column(String, nullable=True)  # ← Новое поле для иконки

    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    discount_price = Column(Float, nullable=True)
    image_url = Column(String, nullable=False)
    weight = Column(String, nullable=False)
    description = Column(Text, nullable=False)

    market_id = Column(Integer, ForeignKey("markets.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    market = relationship("Market", back_populates="products")
    category = relationship("Category", back_populates="products")
