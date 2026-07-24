from fastapi import HTTPException
from app.services.movimientos_service import calcular_monto_visible
from app.mock_data.tarjetas_data import tarjetas
from app.mock_data.movimientos_data import movimientos
from app.mock_data.tipo_tarjeta_data import tipos_tarjetas
from app.mock_data.clientes_data import clientes

from app.services.saldo_service import calcular_saldo_tarjeta


# =====================================================
# OBTENER CATEGORIA CLIENTE
# =====================================================

def obtener_categoria_cliente(cliente_id):

    for cliente in clientes:
        if cliente["id"] == cliente_id:
            return cliente["categoria"]

    return None


# =====================================================
# OBTENER DEFINICION TARJETA
# =====================================================

def obtener_definicion_tarjeta(cliente_categoria, tipo, marca):

    tarjetas_categoria = tipos_tarjetas.get(cliente_categoria)

    if not tarjetas_categoria:
        return None

    tarjetas_tipo = tarjetas_categoria.get(tipo, [])

    for tarjeta in tarjetas_tipo:
        if tarjeta["marca"] == marca:
            return tarjeta

    return None


# =====================================================
# OBTENER TARJETA
# =====================================================

def obtener_tarjeta(tarjeta_id):

    for tarjeta in tarjetas:
        if tarjeta["id"] == tarjeta_id:
            return tarjeta

    raise HTTPException(
        status_code=404,
        detail="Tarjeta no encontrada"
    )


# =====================================================
# OBTENER MOVIMIENTOS TARJETA
# =====================================================

def obtener_lista_movimientos_tarjeta(tarjeta_id):

    movimientos_tarjeta = [

        movimiento

        for movimiento in movimientos

        if movimiento.get("tarjeta_id") == tarjeta_id

    ]

    if not movimientos_tarjeta:

        raise HTTPException(
            status_code=404,
            detail="La tarjeta no posee movimientos"
        )

    movimientos_tarjeta.sort(
        key=lambda x: x["fecha"],
        reverse=True
    )

    return movimientos_tarjeta


# =====================================================
# DETALLE TARJETA + MOVIMIENTOS
# =====================================================

def obtener_movimientos_tarjeta(tarjeta_id: int):

    tarjeta_encontrada = obtener_tarjeta(tarjeta_id)

    movimientos_tarjeta = obtener_lista_movimientos_tarjeta(tarjeta_id)

    for movimiento in movimientos_tarjeta:

        movimiento["monto_visible"] = calcular_monto_visible(movimiento)

    saldo = calcular_saldo_tarjeta(movimientos_tarjeta)

    categoria_cliente = obtener_categoria_cliente(
        tarjeta_encontrada["cliente_id"]
    )

    definicion = obtener_definicion_tarjeta(
        categoria_cliente,
        tarjeta_encontrada["tipo"],
        tarjeta_encontrada["marca"]
    )

    tarjeta_respuesta = {

        "id": tarjeta_encontrada["id"],

        "tipo": tarjeta_encontrada["tipo"],

        "marca": tarjeta_encontrada["marca"],

        "categoria": (
            definicion["categoria"]
            if definicion
            else None
        ),

        "nombre": (
            definicion["nombre"]
            if definicion
            else None
        ),

        "numero": tarjeta_encontrada["numero"],

        "estado": tarjeta_encontrada["estado"],

        "limite": (
            definicion["limite"]
            if definicion and "limite" in definicion
            else None
        ),

        "saldo_pesos": saldo["saldo_pesos"],

        "saldo_dolares": saldo["saldo_dolares"]

    }

    return {

        "tarjeta": tarjeta_respuesta,

        "movimientos": movimientos_tarjeta

    }