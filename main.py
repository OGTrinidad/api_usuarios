
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()

ARCHIVO = "usuarios.json"


# Modelo de datos de un usuario
class Usuario(BaseModel):
    nombre: str
    edad: int


# Cargar usuarios desde el archivo JSON
def cargar_usuarios():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


# Guardar usuarios en el archivo JSON
def guardar_usuarios():
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


usuarios = cargar_usuarios()


@app.get("/")
def inicio():
    return {"mensaje": "API de usuarios funcionando"}


@app.get("/usuarios")
def listar_usuarios():
    if not usuarios:
        return {"mensaje": "no hay usuarios"}

    return usuarios


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    datos = usuario.model_dump()
    usuarios.append(datos)
    guardar_usuarios()
    return datos


@app.delete("/usuarios/{nombre}")
def borrar_usuario(nombre: str):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            usuarios.remove(usuario)
            guardar_usuarios()
            return {"mensaje": f"Usuario {nombre} eliminado"}

    return {"mensaje": f"No existe el usuario {nombre}"}
