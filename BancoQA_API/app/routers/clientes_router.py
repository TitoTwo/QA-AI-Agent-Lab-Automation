from fastapi import APIRouter, HTTPException

from app.mock_data.clientes_data import clientes

from app.services.cliente_service import obtener_resumen_cliente



router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)



@router.get("/")
def obtener_clientes():

    return clientes



@router.get("/{cliente_id}")
def obtener_cliente(cliente_id:int):

    for cliente in clientes:

        if cliente["id"] == cliente_id:

            return cliente


    raise HTTPException(
        status_code=404,
        detail="Cliente no encontrado"
    )



@router.get("/{cliente_id}/resumen")
def obtener_resumen(cliente_id:int):


    resumen = obtener_resumen_cliente(cliente_id)


    if not resumen:

        raise HTTPException(
            status_code=404,
            detail="Cliente no encontrado"
        )


    return resumen