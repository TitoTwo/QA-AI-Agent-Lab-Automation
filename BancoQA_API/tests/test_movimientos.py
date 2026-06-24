from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_movimientos_cuenta():

    response = client.get(
        "/movimientos/cuenta/5001"
    )


    assert response.status_code == 200


    body = response.json()


    assert len(body) == 4




def test_movimientos_tarjeta_debito():

    response = client.get(
        "/movimientos/tarjeta/102"
    )


    assert response.status_code == 200


    body = response.json()


    assert len(body) == 2


    for movimiento in body:

        assert movimiento["tarjeta_id"] == 102




def test_movimientos_tarjeta_credito():

    response = client.get(
        "/movimientos/tarjeta/101"
    )


    assert response.status_code == 200


    body = response.json()


    assert len(body) == 2


    for movimiento in body:

        assert movimiento["tarjeta_id"] == 101




def test_tarjeta_sin_movimientos():

    response = client.get(
        "/movimientos/tarjeta/999"
    )


    assert response.status_code == 404