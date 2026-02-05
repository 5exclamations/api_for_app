from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routers import markets, categories, products

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="Market Price Tracker API",
    version="1.0.0"
)

# CORS for Flutter
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(markets.router)
app.include_router(categories.router)
app.include_router(products.router)

@app.get("/")
def root():
    return {"message": "Market Price Tracker API is running", "docs": "/docs"}
