import pytest
from fastapi.testclient import TestClient
from app.server.server import create_server

@pytest.fixture
def client():
    app = create_server()
    with TestClient(app) as c:
        yield c
