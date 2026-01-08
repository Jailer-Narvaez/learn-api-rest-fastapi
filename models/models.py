from pydantic import BaseModel

class Producto(BaseModel):
    id: int
    name: str
    price: float



class Inventario(BaseModel):
    nombre: str
    precio: float
    en_stock: bool

class Libros(BaseModel):
    id: int
    nombre: str
    genero: str
