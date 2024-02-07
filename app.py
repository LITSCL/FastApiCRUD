from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from uuid import uuid1

app: object = FastAPI(
    title = "API REST",
    description = "Es una simple API REST de prueba creada con el framework FastAPI",
    version = "1.0.0"
)

class Producto(BaseModel):
    codigo: Optional[str] = None
    nombre: str = None
    precio: int = None

productos: list = []

@app.get("/", response_model = List[Producto], tags = ["modelo_producto"])
async def get_productos() -> list:
    return productos

@app.get("/{codigo}", response_model = Producto, tags = ["modelo_producto"])
async def get_producto(codigo: str) -> Producto:
    for producto in productos:
        if (codigo == producto.codigo):
            return producto
    raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el producto con el codigo " + str(codigo))

@app.post("/", response_model = Producto, tags = ["modelo_producto"])
async def post_producto(producto: Producto) -> Producto:
    producto.codigo = str(uuid1())
    productos.append(producto)
    return productos[len(productos) - 1]

@app.put("/{codigo}", response_model = Producto, tags = ["modelo_producto"])
async def put_producto(codigo: str, producto_obtenido: Producto) -> Producto:
    for i, producto in enumerate(productos):
        if (codigo == producto.codigo):
            productos[i].nombre = producto_obtenido.nombre
            productos[i].precio = producto_obtenido.precio
            return producto
    raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el producto con el codigo " + str(codigo))

@app.delete("/{codigo}", response_model = Producto, tags = ["modelo_producto"])
async def delete_producto(codigo: str) -> Producto:
    for i, producto in enumerate(productos):
        if (codigo == producto.codigo):
            productos.pop(i)
            return producto
    raise HTTPException(status_code = 404, detail = "SERVIDOR: No existe el producto con el codigo " + str(codigo))
        
    
    


