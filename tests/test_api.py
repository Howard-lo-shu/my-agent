import importlib.util

import pytest

pytestmark = pytest.mark.skipif(
    not (importlib.util.find_spec("fastapi") and importlib.util.find_spec("httpx")),
    reason="fastapi / httpx not installed",
)


@pytest.fixture
def client():
    from fastapi.testclient import TestClient
    from src.api.app import app
    return TestClient(app)


def test_move_updates_status(client):
    r = client.post("/move", json={"location": "kitchen"})
    assert r.json() == {"result": "Robot moving to kitchen"}
    assert client.get("/status").json() == {"result": "Robot idle at kitchen"}


def test_move_rejects_empty_location(client):
    assert client.post("/move", json={"location": ""}).status_code == 422
