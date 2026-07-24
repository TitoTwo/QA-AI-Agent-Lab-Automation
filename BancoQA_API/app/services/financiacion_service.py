from math import pow
from datetime import datetime
from random import randint


# =====================================================
# TASAS SIMULADAS
# =====================================================

TNA = 60

PLANES = {

    3: {
        "cft": 74
    },

    6: {
        "cft": 81
    },

    12: {
        "cft": 94
    },

    18: {
        "cft": 109
    },

    24: {
        "cft": 122
    }

}


# =====================================================
# SIMULAR FINANCIACIÓN
# =====================================================

def simular_financiacion(request):

    monto = request.monto
    cuotas = request.cuotas

    if cuotas not in PLANES:

        return {
            "error": "Cantidad de cuotas no válida."
        }

    plan = PLANES[cuotas]

    # La simulación usa el CFT anual para calcular la cuota.
    tasa_mensual = (plan["cft"] / 100) / 12

    valor_cuota = (
        monto
        * tasa_mensual
        / (1 - pow((1 + tasa_mensual), -cuotas))
    )

    total = valor_cuota * cuotas

    return {

        "monto": round(monto, 2),

        "cuotas": cuotas,

        "tna": TNA,

        "cft": plan["cft"],

        "valor_cuota": round(valor_cuota, 2),

        "total": round(total, 2)

    }


# =====================================================
# CONFIRMAR FINANCIACIÓN
# =====================================================

def confirmar_financiacion(request):

    simulacion = simular_financiacion(request)

    numero_operacion = str(randint(100000000, 999999999))

    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")

    simulacion["numero_operacion"] = numero_operacion
    simulacion["fecha_operacion"] = fecha

    return simulacion