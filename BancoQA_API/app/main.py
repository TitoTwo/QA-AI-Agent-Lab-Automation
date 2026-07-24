from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import clientes_router
from app.routers import cuentas_router
from app.routers import tarjetas_router
from app.routers import movimientos_router
from app.routers import auth_router
from app.routers import home_router
from app.routers import financiacion_router


app = FastAPI(
    title="BancoQA API",
    description="API bancaria ficticia para automatización QA",
    version="1.0"
)


# Configuración CORS para permitir comunicación con React
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(clientes_router.router)
app.include_router(cuentas_router.router)
app.include_router(tarjetas_router.router)
app.include_router(movimientos_router.router)
app.include_router(auth_router.router)
app.include_router(home_router.router)
app.include_router(financiacion_router.router)