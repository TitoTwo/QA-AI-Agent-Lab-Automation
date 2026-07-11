from fastapi import APIRouter

from app.services.movimientos_service import (
    obtener_todos_movimientos,
    obtener_movimientos_cuenta,
    obtener_movimientos_tarjeta
)



router = APIRouter()



@router.get("/movimientos")
def obtener_movimientos():

    return obtener_todos_movimientos()




@router.get("/movimientos/cuenta/{cuenta_id}")
def movimientos_cuenta(cuenta_id:int):

    return obtener_movimientos_cuenta(cuenta_id)




@router.get("/movimientos/tarjeta/{tarjeta_id}")
def movimientos_tarjeta(tarjeta_id:int):

    return obtener_movimientos_tarjeta(tarjeta_id)