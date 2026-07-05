from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# --- SAMPLE DATA (Hardcoded Inventory) ---
inventory = [
    {"id": 1, "name": "Laptop", "price": 75000, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 1500, "stock": 50},
    {"id": 3, "name": "Keyboard", "price": 3500, "stock": 25}
]

# --- PYDANTIC MODEL (Request Body Validation) ---
class Item(BaseModel):
    id: int
    name: str
    price: float
    stock: int

# 1. GET ALL ITEMS
@app.get("/inventory")
def get_all_items():
    return {"status": "success", "data": inventory}

# 2. GET ITEM BY ID (With Int Type Validation & 404 Error Handling)
@app.get("/inventory/{item_id}")
def get_item_by_id(item_id: int):
    # List mein se item dhoond rahe hain
    for item in inventory:
        if item["id"] == item_id:
            return {"status": "success", "data": item}
    
    # Agar loop khatam ho jaye aur item na mile toh 404 error
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found in inventory")

# 3. POST NEW ITEM (Add to Inventory)
@app.post("/inventory")
def create_item(new_item: Item):
    # Pydantic khud hi input check kar lega, hum bas list mein append karenge
    inventory.append(new_item.model_dump())
    return {"status": "success", "message": "Item added successfully", "data": new_item}
    