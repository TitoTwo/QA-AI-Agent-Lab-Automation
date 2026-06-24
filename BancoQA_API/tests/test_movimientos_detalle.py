from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_movimientos_cuenta():

    response = client.get(
        "/movimientos/cuenta/5001"
    )


    assert response.status_code == 200


    body=response.json()


    assert len(body) == 4



def test_movimientos_tarjeta_debito():

    response = client.get(
        "/movimientos/tarjeta/102"
    )


    assert response.status_code == 200


    body=response.json()


    assert len(body)==2



def test_movimientos_tarjeta_credito():

    response = client.get(
        "/movimientos/tarjeta/101"
    )


    assert response.status_code == 200


    body=response.json()


    assert len(body)==2