from fastapi import FastAPI, HTTPException
from .utils import getRendiciones, createRendicion, updateRendicion, deleteRendicion
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class RendicionCreate(BaseModel):
    fecha: date
    monto: float

class RendicionUpdate(BaseModel):
    fecha: date
    monto: float

@app.get("/")
def status():
    print("Mmmmmm Tato")
    return {"message": "Funcionando"}

@app.get("/rendiciones")
def read_rendiciones():
    rows = getRendiciones()
    return {"message": rows}

@app.post("/rendiciones")
def create_rendicion(rendicion: RendicionCreate):
    new_id = createRendicion(rendicion.fecha, rendicion.monto)
    return {"message": f"Rendicion creada con ID {new_id}"}

@app.put("/rendiciones/{rendicion_id}")
def update_rendicion(rendicion_id: int, rendicion: RendicionUpdate):
    # Primero verificamos si existe la rendición
    updated_rows = updateRendicion(rendicion_id, rendicion.fecha, rendicion.monto)
    if updated_rows == 0:
        # Si no se actualizó ninguna fila, lanzamos una excepción 404
        raise HTTPException(status_code=404, detail=f"Rendicion con ID {rendicion_id} no encontrada")
    
    return {"message": f"Rendicion con ID {rendicion_id} actualizada"}

@app.delete("/rendiciones/{rendicion_id}")
def delete_rendicion(rendicion_id: int):
    deleteRendicion(rendicion_id)
    return {"message": f"Rendicion con ID {rendicion_id} eliminada"}
