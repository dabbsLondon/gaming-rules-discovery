from fastapi.testclient import TestClient
from python_service.app.main import app


def test_health_endpoint():
    client = TestClient(app)
    resp = client.get("/health")
    assert resp.json() == {"status": "ok"}
