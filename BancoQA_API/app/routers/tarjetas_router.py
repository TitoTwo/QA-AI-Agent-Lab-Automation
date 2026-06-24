from fastapi import APIRouter, HTTPException

from app.mock_data.tarjetas_data import tarjetas
from app.mock_data.cuentas_data import cuentas
from app.services.tarjeta_service import obtener_movimientos_tarjeta


router = APIRouter(
    prefix="/tarjetas",
    tags=["Tarjetas"]
)


@router.get("/")
def obtener_tarjetas():

    return tarjetas



@router.get("/cliente/{cliente_id}")
def obtener_tarjetas_cliente(cliente_id:int):

    tarjetas_cliente = []

    for tarjeta in tarjetas:

        if tarjeta["cliente_id"] == cliente_id:
            tarjetas_cliente.append(tarjeta)


    if not tarjetas_cliente:

        raise HTTPException(
            status_code=404,
            detail="Cliente sin tarjetas"
        )


    return tarjetas_cliente



@router.get("/{tarjeta_id}/saldo")
def consultar_saldo_tarjeta(tarjeta_id:int):

    for tarjeta in tarjetas:

        if tarjeta["id"] == tarjeta_id:


            # Tarjeta débito
            if tarjeta["tipo"] == "DEBITO":

                cuenta_id = tarjeta["cuenta_id"]


                for cuenta in cuentas:

                    if cuenta["id"] == cuenta_id:

                        return {
                            "tarjeta_id": tarjeta_id,
                            "cuenta_id": cuenta_id,
                            "saldo": cuenta["saldo"]
                        }


                raise HTTPException(
                    status_code=404,
                    detail="Cuenta asociada no encontrada"
                )


            # Tarjeta crédito
            raise HTTPException(
                status_code=400,
                detail="La tarjeta de crédito no posee saldo"
            )



    raise HTTPException(
        status_code=404,
        detail="Tarjeta no encontrada"
    )


@router.get("/{tarjeta_id}/movimientos")
def movimientos_tarjeta(tarjeta_id:int):

    return obtener_movimientos_tarjeta(tarjeta_id)


@router.get("/{tarjeta_id}")
def obtener_tarjeta(tarjeta_id:int):

    for tarjeta in tarjetas:

        if tarjeta["id"] == tarjeta_id:
            return tarjeta


    raise HTTPException(
        status_code=404,
        detail="Tarjeta no encontrada"
    )