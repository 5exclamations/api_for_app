from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, auth, database

router = APIRouter(prefix="/api/v1/items", tags=["items"])

@router.post("/", response_model=schemas.ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    """Создать новый элемент (требуется авторизация)"""
    db_item = models.Item(**item.dict(), owner_id=current_user.id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[schemas.ItemResponse])
def get_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    """Получить список элементов текущего пользователя"""
    items = db.query(models.Item).filter(
        models.Item.owner_id == current_user.id
    ).offset(skip).limit(limit).all()
    return items

@router.get("/{item_id}", response_model=schemas.ItemResponse)
def get_item(
    item_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    """Получить элемент по ID"""
    item = db.query(models.Item).filter(
        models.Item.id == item_id,
        models.Item.owner_id == current_user.id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(
    item_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    """Удалить элемент"""
    item = db.query(models.Item).filter(
        models.Item.id == item_id,
        models.Item.owner_id == current_user.id
    ).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return None
