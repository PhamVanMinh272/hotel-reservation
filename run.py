# app/__init__.py
import json
import os

from flask import Flask
from app.api import register_api
from app.config import Config
# from .extensions import db  # if you're using SQLAlchemy, for example


def create_app(config_name='development'):
    app = Flask(__name__)

    # Load configuration
    # app.config.from_object(f'app.config.{config_name.capitalize()}Config')
    app.config.from_object(Config)

    # Initialize extensions
    # db.init_app(app)

    # Register API versions
    register_api(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
