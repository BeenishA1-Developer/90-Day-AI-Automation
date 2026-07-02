from fastapi import FastAPI, HTTPException

app = FastAPI()

# Fake database dictionary
fake_products_db = {
    1: {"name": "Laptop", "price": 999.99},
    2: {"name": "Smartphone", "price": 499.99},
    3: {"name": "Headphones", "price": 79.99}
}

@app.get("/")
def read_root():
    return {"message": "Day 24: Virtual Environment & Error Handling active!"}

# Route to get a product by ID with proper HTTPException handling
@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in fake_products_db:
        # Professional 404 error triggering
        raise HTTPException(
            status_code=404, 
            detail=f"Product with ID {product_id} does not exist in our database."
        )
    
    return {
        "status": "success",
        "product": fake_products_db[product_id]
    }