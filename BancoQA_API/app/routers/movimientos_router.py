from fastapi import APIRouter, HTTPException

from app.mock_data.movimientos_data import movimientos


router = APIRouter(
    prefix="/movimientos",
    tags=["Movimientos"]
)


@router.get("/")
def obtener_movimientos():

    return movimientos



@router.get("/cuenta/{cuenta_id}")
def movimientos_cuenta(cuenta_id:int):

    resultado = []

    for movimiento in movimientos:

        if movimiento["cuenta_id"] == cuenta_id:

            resultado.append(movimiento)


    if not resultado:

        raise HTTPException(
            status_code=404,
            detail="Cuenta sin movimientos"
        )


    return resultado



@router.get("/tarjeta/{tarjeta_id}")
def movimientos_tarjeta(tarjeta_id:int):

    resultado = []

    for movimiento in movimientos:

        if movimiento["tarjeta_id"] == tarjeta_id:

            resultado.append(movimiento)


    if not resultado:

        raise HTTPException(
            status_code=404,
            detail="Tarjeta sin movimientos"
        )


    return resultado