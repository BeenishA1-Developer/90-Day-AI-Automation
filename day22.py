from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to AI Automation Week 4!"}

@app.get("/greet/{name}")
def greet_user(name: str):
    return {"message": f"Hello {name}, let's build some powerful APIs!"}