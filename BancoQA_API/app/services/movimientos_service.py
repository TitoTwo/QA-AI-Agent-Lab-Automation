from fastapi import HTTPException

from app.mock_data.movimientos_data import movimientos
from app.mock_data.tarjetas_data import tarjetas
from app.services.saldo_service import calcular_saldo_cuenta



# =====================================================
# TODOS LOS MOVIMIENTOS
# =====================================================

def obtener_todos_movimientos():

    return ordenar_movimientos(
        movimientos
    )





# =====================================================
# BUSCAR TARJETA
# =====================================================

def buscar_tarjeta(tarjeta_id):


    for tarjeta in tarjetas:

        if tarjeta["id"] == tarjeta_id:

            return tarjeta


    return None






# =====================================================
# MOVIMIENTOS CUENTA
# =====================================================

def obtener_movimientos_cuenta(cuenta_id:int):


    resultado=[]



    for movimiento in movimientos:



        # movimientos propios cuenta

        if movimiento.get("cuenta_id") == cuenta_id:

            resultado.append(
                movimiento
            )



        # movimientos tarjeta debito asociados

        elif movimiento.get("tipo") == "TARJETA_DEBITO":


            tarjeta = buscar_tarjeta(
                movimiento.get("tarjeta_id")
            )


            if tarjeta and tarjeta.get("cuenta_id") == cuenta_id:

                resultado.append(
                    movimiento
                )





    if not resultado:


        raise HTTPException(

            status_code=404,

            detail="Cuenta sin movimientos"

        )



    return agregar_saldo_resultante(
        resultado,
        cuenta_id
    )





# =====================================================
# CALCULAR SALDO RESULTANTE CUENTA
# =====================================================

def agregar_saldo_resultante(
        movimientos_cuenta,
        cuenta_id
):


    saldo = calcular_saldo_cuenta(
        cuenta_id
    )


    movimientos_ordenados = sorted(

        movimientos_cuenta,

        key=lambda x:x["fecha"],

        reverse=True

    )


    for movimiento in movimientos_ordenados:


        movimiento["saldo_resultante"] = saldo


        saldo -= movimiento["monto"]



    return movimientos_ordenados





# =====================================================
# MOVIMIENTOS TARJETA
# =====================================================

def obtener_movimientos_tarjeta(tarjeta_id:int):


    tarjeta = buscar_tarjeta(
        tarjeta_id
    )


    if not tarjeta:


        raise HTTPException(

            status_code=404,

            detail="Tarjeta no encontrada"

        )



    movimientos_tarjeta=[]



    for movimiento in movimientos:


        if movimiento.get("tarjeta_id") == tarjeta_id:


            movimientos_tarjeta.append(
                movimiento
            )





    if not movimientos_tarjeta:


        raise HTTPException(

            status_code=404,

            detail="Tarjeta sin movimientos"

        )





    return {


        "tarjeta": tarjeta,


        "movimientos": ordenar_movimientos(
            movimientos_tarjeta
        )

    }





# =====================================================
# ORDEN FECHA
# =====================================================

def ordenar_movimientos(lista):


    return sorted(

        lista,

        key=lambda x:x["fecha"],

        reverse=True

    )

# =====================================================
# CALCULAR VALOR CUOTA
# =====================================================

def calcular_valor_cuota(movimiento):

    cuotas = movimiento.get("cuotas")

    if not cuotas:
        return abs(movimiento["monto"])

    total = cuotas.get("total", 1)

    if total <= 1:
        return abs(movimiento["monto"])

    return round(abs(movimiento["monto"]) / total, 2)


# =====================================================
# CALCULAR MONTO VISIBLE
# =====================================================

def calcular_monto_visible(movimiento):

    cuotas = movimiento.get("cuotas")

    if not cuotas:
        return abs(movimiento["monto"])

    if cuotas["total"] <= 1:
        return abs(movimiento["monto"])

    return calcular_valor_cuota(movimiento)