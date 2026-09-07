from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_create_and_read_task():
    r = client.post("/tasks", json={"title": "Learn Trivy"})
    assert r.status_code == 201
    task_id = r.json()["id"]

    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.json()["title"] == "Learn Trivy"

def test_missing_task_returns_404():
    assert client.get("/tasks/9999").status_code == 404
