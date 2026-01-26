from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(prefix="/api/v1/markets", tags=["markets"])

@router.get("/", response_model=List[schemas.MarketResponse])
def get_markets(db: Session = Depends(database.get_db)):
    """Получить все магазины"""
    return db.query(models.Market).all()

@router.post("/", response_model=schemas.MarketResponse)
def create_market(market: schemas.MarketCreate, db: Session = Depends(database.get_db)):
    """Создать новый магазин"""
    db_market = models.Market(**market.dict())
    db.add(db_market)
    db.commit()
    db.refresh(db_market)
    return db_market
