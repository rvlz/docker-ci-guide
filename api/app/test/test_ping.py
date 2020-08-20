"""/ping endpoint tests."""
import os

url_base = f"/api/{os.getenv('VERSION')}"


def test_ping(client):
    response = client.get(f"{url_base}/ping")
    assert response.status_code == 200
    assert response.data == b"pong"
