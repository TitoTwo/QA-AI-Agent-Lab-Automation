from fastapi import HTTPException

from app.mock_data.cuentas_data import cuentas
from app.mock_data.movimientos_data import movimientos
from app.mock_data.tarjetas_data import tarjetas



def obtener_movimientos_cuenta(cuenta_id:int):


    cuenta_encontrada = None


    # Buscar cuenta

    for cuenta in cuentas:

        if cuenta["id"] == cuenta_id:

            cuenta_encontrada = cuenta
            break



    if not cuenta_encontrada:

        raise HTTPException(
            status_code=404,
            detail="Cuenta no encontrada"
        )



    movimientos_cuenta = []



    # Buscar tarjetas débito asociadas a la cuenta

    tarjetas_debito = []


    for tarjeta in tarjetas:


        if (
            tarjeta["tipo"] == "DEBITO"
            and tarjeta["cuenta_id"] == cuenta_id
        ):

            tarjetas_debito.append(
                tarjeta["id"]
            )



    # Buscar movimientos relacionados

    for movimiento in movimientos:


        # Movimiento propio de la cuenta

        if movimiento["cuenta_id"] == cuenta_id:

            movimientos_cuenta.append(
                movimiento
            )



        # Movimiento generado por tarjeta débito asociada

        elif movimiento["tarjeta_id"] in tarjetas_debito:

            movimientos_cuenta.append(
                movimiento
            )



    # Ordenar del más reciente al más antiguo

    movimientos_cuenta.sort(
        key=lambda x: (
            x["fecha"],
            x["hora"]
        ),
        reverse=True
    )



    return {


        "cuenta": cuenta_encontrada,


        "movimientos": movimientos_cuenta

    }