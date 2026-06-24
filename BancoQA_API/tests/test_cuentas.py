from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_obtener_cuentas():

    response = client.get("/cuentas/")


    assert response.status_code == 200


    body = response.json()


    assert len(body) == 3



def test_obtener_cuenta_existente():

    response = client.get("/cuentas/5001")


    assert response.status_code == 200


    body = response.json()


    assert body["tipo"] == "CAJA_AHORRO"

    assert body["saldo"] == 150000



def test_cuenta_inexistente():

    response = client.get("/cuentas/9999")


    assert response.status_code == 404