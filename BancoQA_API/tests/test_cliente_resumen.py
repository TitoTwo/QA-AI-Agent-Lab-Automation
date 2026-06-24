from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_obtener_resumen_cliente():

    response = client.get(
        "/clientes/1/resumen"
    )


    assert response.status_code == 200


    body = response.json()


    assert body["cliente"]["id"] == 1


    assert len(body["cuentas"]) == 2


    assert len(body["tarjetas"]) == 2




def test_cliente_inexistente_resumen():

    response = client.get(
        "/clientes/999/resumen"
    )


    assert response.status_code == 404


    body = response.json()


    assert body["detail"] == "Cliente no encontrado"