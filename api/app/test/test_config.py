"""Test application configuration."""
import os

from app import create_app

def test_config():
    app = create_app()
    assert app.config["VERSION"] is not None
    assert app.config["SECRET_KEY"] is not None
    assert app.config["VERSION"] == os.getenv("VERSION")
    assert app.config["SECRET_KEY"] == os.getenv("SECRET_KEY")
