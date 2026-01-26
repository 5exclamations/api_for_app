import requests

BASE_URL = "https://api-for-app-r444.onrender.com/api/v1"  # Твой URL

# Создаем магазины
markets = [
    {"name": "Bravo", "logo_url": "https://i.ibb.co/6yYQfCQ/Bravo.png"},
    {"name": "Araz", "logo_url": "https://i.ibb.co/3k0421h/araz.png"},
    {"name": "Oba", "logo_url": "https://i.ibb.co/7jW1bVv/oba.png"},
]

for market in markets:
    requests.post(f"{BASE_URL}/markets/", json=market)

# Создаем категории с иконками (используем Material Icons названия)
categories = [
    {"name": "Dairy", "icon": "local_drink"},
    {"name": "Bakery", "icon": "bakery_dining"},
    {"name": "Meat", "icon": "set_meal"},
    {"name": "Produce", "icon": "eco"},
    {"name": "Pantry", "icon": "kitchen"},
]

for category in categories:
    requests.post(f"{BASE_URL}/categories/", json=category)

# Создаем продукты (добавь все свои продукты)
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
    {
        "name": "Eggs", "price": 2.20, "discount_price": None,
        "market_id": 1, "category_id": 5, "weight": "12 pack",
        "description": "Organic free-range eggs.",
        "image_url": "https://i.ibb.co/d0SM06z/eggs.png"
    },
    # Добавь остальные продукты
]

for product in products:
    try:
        requests.post(f"{BASE_URL}/products/", json=product)
    except Exception as e:
        print(f"Error: {e}")

print("✅ Data seeded successfully!")
