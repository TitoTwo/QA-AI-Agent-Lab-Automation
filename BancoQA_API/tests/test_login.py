from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)



def test_login_exitoso():


    response = client.post(
        "/auth/login",
        params={
            "usuario":"juan.perez",
            "password":"123456"
        }
    )


    assert response.status_code == 200


    body = response.json()


    assert body["mensaje"] == "Login exitoso"

    assert body["cliente_id"] == 1

    assert body["token"] == "TOKEN_DEMO_123"




def test_login_usuario_incorrecto():


    response = client.post(
        "/auth/login",
        params={
            "usuario":"juan.perez",
            "password":"111111"
        }
    )


    assert response.status_code == 401



def test_usuario_bloqueado():


    response = client.post(
        "/auth/login",
        params={
            "usuario":"usuario.bloqueado",
            "password":"999999"
        }
    )


    assert response.status_code == 403