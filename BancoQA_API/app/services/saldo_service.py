from app.mock_data.movimientos_data import movimientos
from app.mock_data.tarjetas_data import tarjetas



# =====================================================
# SALDO TARJETA CREDITO
# =====================================================

def calcular_saldo_tarjeta(movimientos_tarjeta):


    saldo_pesos = 0

    saldo_dolares = 0



    for movimiento in movimientos_tarjeta:


        if movimiento.get("moneda") == "ARS":


            saldo_pesos += abs(
                movimiento["monto"]
            )



        elif movimiento.get("moneda") == "USD":


            saldo_dolares += abs(
                movimiento["monto"]
            )




    return {


        "saldo_pesos": saldo_pesos,


        "saldo_dolares": saldo_dolares


    }





# =====================================================
# BUSCAR TARJETA
# =====================================================

def buscar_tarjeta(tarjeta_id):


    for tarjeta in tarjetas:


        if tarjeta["id"] == tarjeta_id:


            return tarjeta



    return None





# =====================================================
# SALDO ACTUAL CUENTA
# =====================================================

def calcular_saldo_cuenta(cuenta_id):


    saldo = 0



    for movimiento in movimientos:



        incluir_movimiento = False



        # =============================================
        # MOVIMIENTO PROPIO DE CUENTA
        # =============================================


        if movimiento.get("cuenta_id") == cuenta_id:


            incluir_movimiento = True





        # =============================================
        # MOVIMIENTO TARJETA DEBITO
        # =============================================


        elif movimiento.get("tipo") == "TARJETA_DEBITO":



            tarjeta = buscar_tarjeta(

                movimiento.get("tarjeta_id")

            )



            if tarjeta and tarjeta.get("cuenta_id") == cuenta_id:


                incluir_movimiento = True





        if incluir_movimiento:


            saldo += movimiento["monto"]




    return saldo