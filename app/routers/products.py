from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc, asc
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
        on_discount: Optional[bool] = None,
        sort_by: Optional[str] = Query(None, regex="^(price|name|discount)$"),
        sort_order: Optional[str] = Query("asc", regex="^(asc|desc)$"),
        db: Session = Depends(database.get_db)
):
    query = db.query(models.Product)

    if search:
        search_filter = or_(
            models.Product.name.ilike(f"%{search}%"),
            models.Product.description.ilike(f"%{search}%")
        )
        query = query.filter(search_filter)

    if category_id:
        query = query.filter(models.Product.category_id == category_id)

    if market_id:
        query = query.filter(models.Product.market_id == market_id)

    if on_discount:
        query = query.filter(models.Product.discount_price.isnot(None))

    if sort_by:
        if sort_by == "price":
            sort_field = models.Product.price
        elif sort_by == "name":
            sort_field = models.Product.name
        elif sort_by == "discount":
            sort_field = models.Product.price - models.Product.discount_price

        if sort_order == "desc":
            query = query.order_by(desc(sort_field))
        else:
            query = query.order_by(asc(sort_field))

    return query.offset(skip).limit(limit).all()


@router.get("/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(database.get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(database.get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
