from fastapi import HTTPException

from app.mock_data.clientes_data import clientes
from app.mock_data.cuentas_data import cuentas
from app.mock_data.tarjetas_data import tarjetas
from app.mock_data.tipo_tarjeta_data import tipos_tarjetas
from app.services.saldo_service import (
    calcular_saldo_tarjeta,
    calcular_saldo_cuenta
)
from app.mock_data.movimientos_data import movimientos



# =====================================================
# Buscar definición de tarjeta según categoría cliente
# =====================================================

def obtener_tipo_tarjeta(categoria_cliente, tipo, marca):


    tarjetas_categoria = tipos_tarjetas.get(
        categoria_cliente
    )


    if not tarjetas_categoria:

        return None



    tarjetas_tipo = tarjetas_categoria.get(
        tipo,
        []
    )



    for tarjeta in tarjetas_tipo:


        if tarjeta["marca"] == marca:

            return tarjeta



    return None





# =====================================================
# Home del cliente
# =====================================================

def obtener_home_cliente(cliente_id:int):


    cliente_encontrado = None



    # Buscar cliente

    for cliente in clientes:


        if cliente["id"] == cliente_id:

            cliente_encontrado = cliente

            break




    if not cliente_encontrado:


        raise HTTPException(

            status_code=404,

            detail="Cliente no encontrado"

        )




    # =====================================================
    # CUENTAS
    # =====================================================


    cuentas_cliente = []



    for cuenta in cuentas:


        if cuenta["cliente_id"] == cliente_id:



            cuenta_resumen = {


                "id": cuenta["id"],

                "nombre": cuenta["nombre"],

                "moneda": cuenta["moneda"],

                "saldo": calcular_saldo_cuenta(cuenta["id"])

            }



            if "acuerdo" in cuenta:


                cuenta_resumen["acuerdo"] = cuenta["acuerdo"]



            cuentas_cliente.append(

                cuenta_resumen

            )





    # Orden requerido banco

    orden_cuentas = {


        "Caja de Ahorro en pesos":1,

        "Caja de Ahorro en dólares":2,

        "Caja de Ahorro en euros":3,

        "Cuenta Corriente en pesos":4

    }




    cuentas_cliente.sort(

        key=lambda x:

        orden_cuentas.get(

            x["nombre"],

            99

        )

    )







    # =====================================================
    # TARJETAS
    # =====================================================


    tarjetas_cliente = []



    for tarjeta in tarjetas:



        if tarjeta["cliente_id"] == cliente_id:



            definicion_tarjeta = obtener_tipo_tarjeta(


                cliente_encontrado["categoria"],


                tarjeta["tipo"],


                tarjeta["marca"]


            )



            # Si no existe combinación categoría/marca/tipo

            # no se muestra

            if not definicion_tarjeta:


                continue





            tarjeta_resumen = {


                "id": tarjeta["id"],


                "tipo": tarjeta["tipo"],


                "marca": tarjeta["marca"],


                "categoria": definicion_tarjeta["categoria"],


                "nombre": definicion_tarjeta["nombre"],


                "numero": tarjeta["numero"],


                "estado": tarjeta["estado"]


            }




            # Datos exclusivos crédito

            if tarjeta["tipo"] == "CREDITO":


                movimientos_tarjeta = []


                for movimiento in movimientos:


                    if movimiento.get("tarjeta_id") == tarjeta["id"]:

                        movimientos_tarjeta.append(
                            movimiento
                        )



                saldo = calcular_saldo_tarjeta(
                    movimientos_tarjeta
                )



                tarjeta_resumen["limite"] = definicion_tarjeta["limite"]


                tarjeta_resumen["saldo_pesos"] = saldo["saldo_pesos"]


                tarjeta_resumen["saldo_dolares"] = saldo["saldo_dolares"]





            tarjetas_cliente.append(

                tarjeta_resumen

            )








    # Orden bancario

    # 1 Visa crédito

    # 2 Mastercard crédito

    # 3 Visa débito


    orden_tarjetas = {


        ("CREDITO","VISA"):1,


        ("CREDITO","MASTERCARD"):2,


        ("DEBITO","VISA"):3


    }





    tarjetas_cliente.sort(


        key=lambda x:


        orden_tarjetas.get(


            (

                x["tipo"],

                x["marca"]

            ),


            99


        )


    )







    # =====================================================
    # Respuesta final
    # =====================================================


    return {


        "cliente": {


            "id": cliente_encontrado["id"],

            "nombre": cliente_encontrado["nombre"],

            "categoria": cliente_encontrado["categoria"]

        },


        "cuentas": cuentas_cliente,


        "tarjetas": tarjetas_cliente


    }