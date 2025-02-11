from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

# Fake database in memory (for testing purposes)
fake_db = {}

# Pydantic model for Item
class Item(BaseModel):
    id: int
    name: str
    description: str = None
    price: float

# ------------------------------------ CRUD Operations ---------------------------------



# POST: Creates a new item
@app.post("/items")
def create_item(item: Item):
    if item.id in fake_db:
        raise HTTPException(status_code=400, detail="El elemento ya existe.")
    fake_db[item.id] = item
    return {"message": "Elemento creado correctamente.", "item": item}

# GET: Returns welcome msj
@app.get("/")
def read_root():
    return {"message": "¡Hola! Bienvenido a tu primera API con FastAPI."}

# GET with optional parameter: Returns welcome msj with name
@app.get("/greeting")
def read_saludo(name: str = "usuario"):
    return {"mensaje": f"Hola, {name}. ¡Espero que disfrutes la API!"}