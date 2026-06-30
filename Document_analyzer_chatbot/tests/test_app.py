from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_upload_and_chat_flow():
    files = {"files": ("sample.txt", BytesIO(b"FastAPI is a modern web framework for building APIs with Python. It supports async endpoints and automatic validation."), "text/plain")}

    upload_response = client.post("/documents/upload", files=files)
    assert upload_response.status_code == 200
    payload = upload_response.json()
    assert payload["documents_uploaded"] == 1

    chat_response = client.post(
        "/chat",
        json={"message": "What does the document say about FastAPI?"},
    )
    assert chat_response.status_code == 200
    body = chat_response.json()
    assert "answer" in body
    assert body["answer"]


def test_frontend_index_served():
    response = client.get("/")
    assert response.status_code == 200
    assert "Document Analyzer" in response.text
