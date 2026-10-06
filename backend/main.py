from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import conectar

app = FastAPI()

# Permitir que el frontend se comunique con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Usuario(BaseModel):
    nombre: str
    email: str


@app.post("/usuarios")
def crear_usuario(usuario: Usuario):
    db = conectar()
    cursor = db.cursor()

    sql = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
    valores = (usuario.nombre, usuario.email)

    cursor.execute(sql, valores)
    db.commit()

    cursor.close()
    db.close()

    return {"mensaje": "Usuario creado correctamente"}


@app.get("/usuarios")
def obtener_usuarios():
    db = conectar()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    db.close()

    return usuarios