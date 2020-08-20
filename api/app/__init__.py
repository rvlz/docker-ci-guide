import os

from flask import Flask

from .ping import bp as ping_bp


def create_app():
    """App factory"""
    app = Flask(__name__)
    app.config.from_object("app.config.Config")
    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register blueprints"""
    url_base = f"/api/{app.config['VERSION']}"
    app.register_blueprint(ping_bp, url_prefix=f"{url_base}/ping")
