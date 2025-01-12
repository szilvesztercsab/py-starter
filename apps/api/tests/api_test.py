from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_no_index():
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}


def test_status_ok():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
