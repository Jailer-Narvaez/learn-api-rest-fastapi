from fastapi import Query, HTTPException, APIRouter
from models.models import Libros
from database.database import libros
from typing import List

router = APIRouter(
    prefix="/libros",
    tags=["Libros"]
)

#crud básico
@router.get("/libros", response_model=List[Libros])
def listar_libros():
    return libros 

@router.post("/libros")
def crear_libros(libro: Libros):
    return libro 

@router.put("/libros/{id}", response_model=Libros)
def actualizar_libro(id: int, libro_actualizado: Libros):
    for index, libro in enumerate(libros):
        if libro["id"] == id:
            libros[index] = libro_actualizado.dict()
            return libros[index]


#ejercicio manejo de errores        
@router.delete("/libros/{id}")
def eliminar_libro(id: int):
    for index, libro in enumerate(libros):
        if libro["id"] == id:
            libros.pop(index)
            return {"mensaje": "Libro eliminado correctamente"}
    raise HTTPException(status_code=404, detail="Libro no encontrado") #manejo de errores