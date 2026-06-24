from fastapi import HTTPException

from app.mock_data.clientes_data import clientes
from app.mock_data.cuentas_data import cuentas
from app.mock_data.tarjetas_data import tarjetas



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



    # Buscar cuentas
    cuentas_cliente = []


    for cuenta in cuentas:

        if cuenta["cliente_id"] == cliente_id:

            cuentas_cliente.append(
                {
                    "id": cuenta["id"],
                    "tipo": cuenta["tipo"],
                    "moneda": cuenta["moneda"],
                    "saldo": cuenta["saldo"]
                }
            )



    # Buscar tarjetas
    tarjetas_cliente = []


    for tarjeta in tarjetas:


        if tarjeta["cliente_id"] == cliente_id:


            tarjeta_resumen = {

                "id": tarjeta["id"],
                "tipo": tarjeta["tipo"],
                "marca": tarjeta["marca"],
                "numero": tarjeta["numero"],
                "estado": tarjeta["estado"]

            }


            # Si es crédito agregamos datos propios
            if tarjeta["tipo"] == "CREDITO":

                tarjeta_resumen["limite"] = tarjeta["limite"]
                tarjeta_resumen["disponible"] = tarjeta["disponible"]



            # Si es débito buscamos saldo de cuenta asociada
            if tarjeta["tipo"] == "DEBITO":


                cuenta_id = tarjeta["cuenta_id"]


                for cuenta in cuentas:


                    if cuenta["id"] == cuenta_id:


                        tarjeta_resumen["saldo"] = cuenta["saldo"]


            tarjetas_cliente.append(tarjeta_resumen)



    return {


        "cliente": cliente_encontrado,


        "cuentas": cuentas_cliente,


        "tarjetas": tarjetas_cliente


    }