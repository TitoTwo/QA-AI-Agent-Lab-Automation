from fastapi import APIRouter

from app.services.home_service import obtener_home_cliente



router = APIRouter(

    prefix="/clientes",
    tags=["Home Cliente"]

)



@router.get("/{cliente_id}/home")
def home_cliente(cliente_id:int):


    return obtener_home_cliente(cliente_id)