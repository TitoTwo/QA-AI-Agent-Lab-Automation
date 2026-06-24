from fastapi import HTTPException

from app.mock_data.tarjetas_data import tarjetas
from app.mock_data.movimientos_data import movimientos



def obtener_movimientos_tarjeta(tarjeta_id:int):


    tarjeta_encontrada = None


    # Buscar tarjeta

    for tarjeta in tarjetas:

        if tarjeta["id"] == tarjeta_id:

            tarjeta_encontrada = tarjeta
            break



    if not tarjeta_encontrada:

        raise HTTPException(
            status_code=404,
            detail="Tarjeta no encontrada"
        )



    movimientos_tarjeta = []



    # Buscar movimientos asociados a la tarjeta

    for movimiento in movimientos:


        if movimiento["tarjeta_id"] == tarjeta_id:

            movimientos_tarjeta.append(
                movimiento
            )



    # Si no tiene movimientos

    if not movimientos_tarjeta:

        raise HTTPException(
            status_code=404,
            detail="La tarjeta no posee movimientos"
        )



    # Ordenar del más reciente al más antiguo

    movimientos_tarjeta.sort(
        key=lambda x: (
            x["fecha"],
            x["hora"]
        ),
        reverse=True
    )



    return {


        "tarjeta": tarjeta_encontrada,


        "movimientos": movimientos_tarjeta

    }