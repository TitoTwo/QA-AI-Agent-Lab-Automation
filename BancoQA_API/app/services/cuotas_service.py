from app.services.tarjeta_service import obtener_lista_movimientos_tarjeta


# =====================================================
# CALCULAR VALOR CUOTA
# =====================================================

def calcular_valor_cuota(movimiento):

    total = movimiento["cuotas"]["total"]

    monto_total = abs(movimiento["monto"])

    return round(monto_total / total, 2)


# =====================================================
# CALCULAR CUOTAS RESTANTES
# =====================================================

def calcular_restante(movimiento):

    total = movimiento["cuotas"]["total"]

    actual = movimiento["cuotas"]["actual"]

    restantes = total - actual

    if restantes < 0:
        restantes = 0

    return restantes


# =====================================================
# OBTENER CUOTAS PENDIENTES
# =====================================================

def obtener_cuotas_pendientes(tarjeta_id):

    movimientos = obtener_lista_movimientos_tarjeta(tarjeta_id)

    cuotas_pendientes = []

    proximo_vencimiento = 0

    restante_total = 0

    for movimiento in movimientos:

        if movimiento["tipo"] != "TARJETA_CREDITO":
            continue

        if movimiento["moneda"] != "ARS":
            continue

        if "cuotas" not in movimiento:
            continue

        total = movimiento["cuotas"]["total"]

        if total <= 1:
            continue

        actual = movimiento["cuotas"]["actual"]

        if actual >= total:
            continue

        valor_cuota = calcular_valor_cuota(movimiento)

        cuotas_restantes = calcular_restante(movimiento)

        restante = round(
            valor_cuota * cuotas_restantes,
            2
        )

        cuotas_pendientes.append({

            "id": movimiento["id"],

            "fecha": movimiento["fecha"],

            "movimiento": movimiento["descripcion"],

            "comercio": movimiento["comercio"],

            "moneda": movimiento["moneda"],

            "cuota": f"{actual + 1}/{total}",

            "monto_cuota": valor_cuota,

            "restante": restante

        })

        proximo_vencimiento += valor_cuota

        restante_total += restante

    cuotas_pendientes.sort(
        key=lambda x: x["fecha"],
        reverse=True
    )

    return {

        "proximo_vencimiento": round(
            proximo_vencimiento,
            2
        ),

        "restante_total": round(
            restante_total,
            2
        ),

        "cuotas": cuotas_pendientes

    }