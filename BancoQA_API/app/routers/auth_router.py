from fastapi import APIRouter
from pydantic import BaseModel

from app.services.auth_service import login_usuario


router = APIRouter(
    prefix="/auth",
    tags=["Autenticacion"]
)


# =====================================================
# REQUEST
# =====================================================

class LoginRequest(BaseModel):

    tipo_documento: str
    documento: str
    usuario: str
    password: str


# =====================================================
# LOGIN
# =====================================================

@router.post("/login")
def login(request: LoginRequest):

    return login_usuario(request)