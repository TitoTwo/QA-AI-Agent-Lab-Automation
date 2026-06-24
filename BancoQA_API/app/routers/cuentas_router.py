from fastapi import APIRouter, HTTPException

from app.services.cuenta_service import obtener_movimientos_cuenta
from app.mock_data.cuentas_data import cuentas


router = APIRouter(
    prefix="/cuentas",
    tags=["Cuentas"]
)


@router.get("/")
def obtener_cuentas():

    return cuentas


@router.get("/{cuenta_id}")
def obtener_cuenta(cuenta_id: int):

    for cuenta in cuentas:

        if cuenta["id"] == cuenta_id:
            return cuenta

    raise HTTPException(
        status_code=404,
        detail="Cuenta no encontrada"
    )


@router.get("/{cuenta_id}/movimientos")
def movimientos_cuenta(cuenta_id:int):

    return obtener_movimientos_cuenta(cuenta_id)