# day23.py — FastAPI: Query Parameters + Request Body
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1. Pydantic Model for POST Request Body
class Product(BaseModel):
    name: str
    price: float

# 2. GET Route with Query Parameters (/search)
@app.get("/search")
def search_items(keyword: str = "pizza", limit: int = 5):
    return {
        "status": "success",
        "query_received": {
            "keyword": keyword,
            "limit": limit
        },
        "results": f"Found {limit} items matching '{keyword}'"
    }

# 3. POST Route accepting JSON Body (/products)
@app.get("/")
def read_root():
    return {"message": "Welcome to Day 23 FastAPI basics!"}

@app.post("/products")
def create_product(product: Product):
    return {
        "status": "Product added successfully",
        "data": {
            "product_name": product.name,
            "product_price": product.price
        }
    }