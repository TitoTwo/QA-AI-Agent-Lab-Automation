from fastapi import HTTPException

from app.mock_data.clientes_data import clientes
from app.mock_data.usuarios_data import usuarios

from app.constants.mensajes_login import (
    LOGIN_INVALIDO,
    LOGIN_EXITOSO,
    USUARIO_BLOQUEADO
)


# =====================================================
# LOGIN
# =====================================================

def login_usuario(request):

    print("\n========== REQUEST ==========")
    print("Tipo documento:", request.tipo_documento)
    print("Documento:", request.documento)
    print("Usuario:", request.usuario)
    print("Password:", request.password)

    # ==========================================
    # Buscar cliente
    # ==========================================

    cliente = next(

        (

            c for c in clientes

            if (
                c["tipo_documento"] == request.tipo_documento
                and c["documento"] == request.documento
            )

        ),

        None

    )

    print("\n========== CLIENTE ==========")
    print(cliente)

    if cliente is None:

        raise HTTPException(
            status_code=401,
            detail=LOGIN_INVALIDO
        )

    # ==========================================
    # Buscar usuario
    # ==========================================

    usuario = next(

        (

            u for u in usuarios

            if (
                u["usuario"] == request.usuario
                and u["cliente_id"] == cliente["id"]
            )

        ),

        None

    )

    print("\n========== USUARIO ==========")
    print(usuario)

    if usuario is None:

        raise HTTPException(
            status_code=401,
            detail=LOGIN_INVALIDO
        )

    # ==========================================
    # Validar contraseña
    # ==========================================

    print("\n========== PASSWORD ==========")
    print("Password mock:", usuario["password"])
    print("Password recibida:", request.password)

    if usuario["password"] != request.password:

        raise HTTPException(
            status_code=401,
            detail=LOGIN_INVALIDO
        )

    # ==========================================
    # Usuario bloqueado
    # ==========================================

    print("\n========== ESTADO ==========")
    print(usuario["estado"])

    if usuario["estado"] != "ACTIVO":

        raise HTTPException(
            status_code=403,
            detail=USUARIO_BLOQUEADO
        )

    # ==========================================
    # Login exitoso
    # ==========================================

    print("\n========== LOGIN OK ==========")

    return {

        "success": True,

        "mensaje": LOGIN_EXITOSO,

        "token": "TOKEN_DEMO_123",

        "cliente": {

            "id": cliente["id"],

            "nombre": cliente["nombre"],

            "categoria": cliente["categoria"]

        }

    }