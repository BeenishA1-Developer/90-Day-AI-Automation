from fastapi import FastAPI

app = FastAPI()

# Humne item_id: int likha hai, yaani sirf number chalega!
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {
        "status": "success",
        "message": f"Item {item_id} successfully fetched!",
        "item_id": item_id
    }