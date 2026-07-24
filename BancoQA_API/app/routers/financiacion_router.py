from fastapi import APIRouter
from pydantic import BaseModel

from app.services.financiacion_service import simular_financiacion

router = APIRouter(
    prefix="/financiacion",
    tags=["Financiación"]
)

from app.services.financiacion_service import (
    simular_financiacion,
    confirmar_financiacion
)


# =====================================================
# REQUEST
# =====================================================

class SimulacionRequest(BaseModel):

    monto: float
    cuotas: int


# =====================================================
# SIMULAR FINANCIACIÓN
# =====================================================

@router.post("/simular")
def simular(request: SimulacionRequest):

    return simular_financiacion(request)

# =====================================================
# CONFIRMAR FINANCIACIÓN
# =====================================================

@router.post("/confirmar")
def confirmar(request: SimulacionRequest):

    return confirmar_financiacion(request)