
from fastapi import FastAPI

app = FastAPI()

usuarios = []


@app.get("/")
def inicio():
    return {"mensaje": "API de usuarios funcionando"}


@app.get("/usuarios")
def listar_usuarios():
    if not usuarios:
        return {"mensaje": "no hay usuarios"}

    return usuarios


@app.post("/usuarios")
def crear_usuario(nombre: str, edad: int):
    usuario = {"nombre": nombre, "edad": edad}
    usuarios.append(usuario)
    return usuario


@app.delete("/usuarios/{nombre}")
def borrar_usuario(nombre: str):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            usuarios.remove(usuario)
            return {"mensaje": f"Usuario {nombre} eliminado"}

    return {"mensaje": f"No existe el usuario {nombre}"}
