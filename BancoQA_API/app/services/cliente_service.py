from app.mock_data.clientes_data import clientes
from app.mock_data.cuentas_data import cuentas
from app.mock_data.tarjetas_data import tarjetas



def obtener_resumen_cliente(cliente_id:int):

    cliente_encontrado = None

    for cliente in clientes:

        if cliente["id"] == cliente_id:

            cliente_encontrado = cliente
            break


    if not cliente_encontrado:

        return None



    cuentas_cliente = []

    for cuenta in cuentas:

        if cuenta["cliente_id"] == cliente_id:

            cuentas_cliente.append(cuenta)



    tarjetas_cliente = []

    for tarjeta in tarjetas:

        if tarjeta["cliente_id"] == cliente_id:

            tarjetas_cliente.append(tarjeta)



    return {

        "cliente": cliente_encontrado,

        "cuentas": cuentas_cliente,

        "tarjetas": tarjetas_cliente

    }