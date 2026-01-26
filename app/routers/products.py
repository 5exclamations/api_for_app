from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import models, schemas, database

router = APIRouter(prefix="/api/v1/products", tags=["products"])


@router.get("/", response_model=List[schemas.ProductResponse])
def get_products(
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None,
        category_id: Optional[int] = None,
        market_id: Optional[int] = None,
        db: Session = Depends(database.get_db)
):
    """Получить продукты с фильтрами"""
    query = db.query(models.Product)

    if search:
        query = query.filter(models.Product.name.ilike(f"%{search}%"))
    if category_id:
        query = query.filter(models.Product.category_id == category_id)
    if market_id:
        query = query.filter(models.Product.market_id == market_id)

    return query.offset(skip).limit(limit).all()


@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(database.get_db)):
    """Получить продукт по ID"""
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    """Создать новый продукт"""
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
