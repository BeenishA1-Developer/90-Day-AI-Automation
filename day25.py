from fastapi import FastAPI

app = FastAPI()

# --- CASE 2: Static Route UPAR, Dynamic Route NEECHE ---

@app.get("/products/featured")
def get_featured_products():
    return {
        "status": "success",
        "message": "List of featured products"
    }

@app.get("/products/{product_id}")
def get_product(product_id: str):
    return {
        "message": "Landed inside Dynamic Route",
        "captured_value": product_id
    }