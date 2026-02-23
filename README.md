<div align="center">

# Market Price Tracker API


    Flutter client app: https://github.com/5exclamations/product_app

    This API is built to power the Market Price Tracker mobile app.


FastAPI backend for a Flutter app that tracks product prices across markets — with filtering, searching, sorting, and discount support.

<img src="https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
<img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00" alt="SQLAlchemy" />
<img src="https://img.shields.io/badge/Pydantic-Schemas-E92063" alt="Pydantic" />
<img src="https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white" alt="SQLite" />
<img src="https://img.shields.io/badge/Auth-JWT-111827" alt="JWT" />
<img src="https://img.shields.io/badge/OpenAPI-%2Fdocs-1f2937" alt="OpenAPI" />

</div>

---

## Overview

This service exposes a REST API to manage **markets**, **categories**, and **products**.
It supports real-world catalog use cases: search by text, filter by market/category, show only discounted items, and sort results.

## Key features

- REST endpoints for Markets / Categories / Products.
- Search across product `name` and `description` (case-insensitive).
- Filters: `category_id`, `market_id`, `on_discount`.
- Sorting: `price`, `name`, or computed `discount` with `asc/desc`.
- Typed request/response schemas with Pydantic and nested responses (Product includes Market + Category).
- CORS enabled.

## API routes

Base:
- `/` — health check message + docs hint
- `/docs` — interactive Swagger UI (OpenAPI)

### Markets
- `GET /api/v1/markets/` — list markets
- `POST /api/v1/markets/` — create market

### Categories
- `GET /api/v1/categories/` — list categories
- `POST /api/v1/categories/` — create category

### Products
- `GET /api/v1/products/` — list products with query params:
  - `skip` (default 0), `limit` (default 100)
  - `search` (matches name/description)
  - `category_id`
  - `market_id`
  - `on_discount=true` (only products with `discount_price != null`)
  - `sort_by=price|name|discount`
  - `sort_order=asc|desc`
- `GET /api/v1/products/{product_id}` — product details
- `POST /api/v1/products/` — create product

Example:
```bash
http://localhost:8000/api/v1/products/?search=milk&market_id=1&on_discount=true&sort_by=price&sort_order=asc
```
Auth (optional / in progress)

The project includes JWT-based auth utilities (HTTPBearer) and user-scoped item endpoints:

    Items are created with owner_id=current_user.id

    All item reads/deletes are restricted to the authenticated owner

Data model

    Market: id, name, logo_url

    Category: id, name, icon?

    Product: id, name, price, discount_price?, image_url, weight, description,
    market_id -> Market, category_id -> Category

SQLite database file:

    sqlite:///./products.db

Local setup

  Create & activate venv, install deps:

        pip install -r requirements.txt
  Run API:

        uvicorn app.main:app --reload
  Open:

        Swagger UI: http://localhost:8000/docs


This backend demonstrates practical API engineering: queryable catalog endpoints, clean schema boundaries, ORM models with relationships, CORS for mobile clients, and a foundation for JWT auth + user isolation.
It’s built to be extendable (pagination, admin-only create routes, price history tables, caching, rate limits, etc.).
