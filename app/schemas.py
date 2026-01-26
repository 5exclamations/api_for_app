from pydantic import BaseModel
from typing import Optional


# Market schemas
class MarketBase(BaseModel):
    name: str
    logo_url: str


class MarketCreate(MarketBase):
    pass


class MarketResponse(MarketBase):
    id: int

    class Config:
        from_attributes = True


# Category schemas
class CategoryBase(BaseModel):
    name: str
    icon: Optional[str] = None  # ← Новое поле


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int

    class Config:
        from_attributes = True


# Product schemas
class ProductBase(BaseModel):
    name: str
    price: float
    discount_price: Optional[float] = None
    image_url: str
    weight: str
    description: str
    market_id: int
    category_id: int


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    market: MarketResponse
    category: CategoryResponse

    class Config:
        from_attributes = True
