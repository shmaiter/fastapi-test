from fastapi import FastAPI

app = FastAPI()

# Path GET: Returns welcome msj
@app.get("/")
def read_root():
    return {"message": "¡Hola! Bienvenido a tu primera API con FastAPI."}

# Path GET with optional parameter: Returns welcome msj with name
@app.get("/greeting")
def read_saludo(name: str = "usuario"):
    return {"mensaje": f"Hola, {name}. ¡Espero que disfrutes la API!"}