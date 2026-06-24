from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_cliente_consulta_tarjetas():

    response = client.get("/tarjetas/cliente/1")


    assert response.status_code == 200


    body = response.json()


    assert len(body) == 2


    assert body[0]["tipo"] == "CREDITO"

    assert body[0]["estado"] == "ACTIVA"



def test_cliente_sin_tarjetas():

    response = client.get("/tarjetas/cliente/999")


    assert response.status_code == 404


    body = response.json()


    assert body["detail"] == "Cliente sin tarjetas"



def test_consultar_tarjeta():

    response = client.get("/tarjetas/101")


    assert response.status_code == 200


    body = response.json()


    assert body["id"] == 101

    assert body["marca"] == "VISA"

def test_consultar_saldo_tarjeta_debito():

    response = client.get(
        "/tarjetas/102/saldo"
    )


    assert response.status_code == 200


    body=response.json()


    assert body["cuenta_id"] == 5001

    assert body["saldo"] == 150000



def test_tarjeta_credito_no_tiene_saldo():

    response = client.get(
        "/tarjetas/101/saldo"
    )


    assert response.status_code == 400