from fastapi import APIRouter, HTTPException

from app.mock_data.usuarios_data import usuarios
from app.mock_data.clientes_data import clientes


router = APIRouter(
    prefix="/auth",
    tags=["Autenticacion"]
)



@router.post("/login")
def login(usuario:str, password:str):


    usuario_encontrado = None


    for user in usuarios:

        if (
            user["usuario"] == usuario
            and user["password"] == password
        ):
            usuario_encontrado = user
            break



    if usuario_encontrado is None:

        raise HTTPException(
            status_code=401,
            detail="Usuario o contraseña incorrectos"
        )



    if usuario_encontrado["estado"] != "ACTIVO":

        raise HTTPException(
            status_code=403,
            detail="Usuario bloqueado"
        )



    cliente = None


    for c in clientes:

        if c["id"] == usuario_encontrado["cliente_id"]:
            cliente = c
            break



    return {

        "mensaje": "Login exitoso",
        "token": "TOKEN_DEMO_123",
        "cliente_id": cliente["id"],
        "nombre": cliente["nombre"]

    }