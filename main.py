from fastapi import FastAPI
from routers.libros import router

app = FastAPI()

app.include_router(router)
        
#Buenas prácticas
"""
- Separar rutas por módulos (models, database, routes etc...)
- Documentación con OpenApi (docs, tags)
- Validación estricta de datos
- Configuración de errores con HTTPException
"""

