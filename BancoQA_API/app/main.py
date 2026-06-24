from fastapi import FastAPI

from app.routers import clientes_router
from app.routers import cuentas_router
from app.routers import tarjetas_router
from app.routers import movimientos_router
from app.routers import auth_router
from app.routers import home_router


app = FastAPI(
    title="BancoQA API",
    description="API bancaria ficticia para automatización QA",
    version="1.0"
)


app.include_router(clientes_router.router)
app.include_router(cuentas_router.router)
app.include_router(tarjetas_router.router)
app.include_router(movimientos_router.router)
app.include_router(auth_router.router)
app.include_router(home_router.router)