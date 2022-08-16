from fastapi.testclient import TestClient

from src.main import app


client = TestClient(app)


def test_login() -> None:
    response = client.post(
        '/login',
        json={'username': 'stivenramireza', 'password': 'stivenramireza'},
    )
    assert response.status_code == 200
    assert response.json() == {
        'access_token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'
    }
