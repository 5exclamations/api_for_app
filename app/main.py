from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database1
from .routers import markets, categories, products

# Создать таблицы
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Market Price Tracker API",
    version="1.0.0"
)

# CORS для Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключить роутеры
app.include_router(markets.router)
app.include_router(categories.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Market Price Tracker API is running", "docs": "/docs"}
