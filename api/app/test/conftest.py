"""Defines fixtures available to all tests."""
import pytest

from app import create_app


@pytest.fixture
def client():
    """Create test client."""
    app = create_app()
    _client = app.test_client()

    with app.app_context():
        yield _client
