import requests

BASE_URL = "https://api-for-app-r444.onrender.com/api/v1"

# Создаем магазины
markets = [
    {"name": "Ravo", "logo_url": "https://i.ibb.co/6yYQfCQ/ravo.png"},
    {"name": "Araz", "logo_url": "https://i.ibb.co/3k0421h/araz.png"},
    {"name": "Oba", "logo_url": "https://i.ibb.co/7jW1bVv/oba.png"},
]

for market in markets:
    requests.post(f"{BASE_URL}/markets/", json=market)

# Создаем категории
categories = [
    {"name": "Dairy"},
    {"name": "Bakery"},
    {"name": "Meat"},
    {"name": "Produce"},
    {"name": "Pantry"},
]

for category in categories:
    requests.post(f"{BASE_URL}/categories/", json=category)

# Создаем продукты
products = [
    {
        "name": "Milk", "price": 1.50, "discount_price": 1.35,
        "market_id": 1, "category_id": 1, "weight": "1L",
        "description": "Fresh cow milk, pasteurized.",
        "image_url": "https://i.ibb.co/g9f2sWv/milk.png"
    },
    {
        "name": "Bread", "price": 0.80, "discount_price": None,
        "market_id": 1, "category_id": 2, "weight": "500g",
        "description": "Freshly baked white bread.",
        "image_url": "https://i.ibb.co/Jqc34b3/bread.png"
    },
    # Добавь остальные продукты аналогично
]

for product in products:
    requests.post(f"{BASE_URL}/products/", json=product)

print("✅ Data seeded successfully!")
