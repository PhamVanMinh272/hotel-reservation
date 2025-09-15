
from flask import Blueprint
from flask import Flask
from app.api.v1.routes.hotels import hotels_bp

def register_api(app):
    from .v1.routes.hotels import hotels_bp as v1_hotels
    # from .v2.routes.hotels import hotels_bp as v2_hotels

    app.register_blueprint(v1_hotels, url_prefix='/api/v1/hotels')
    # app.register_blueprint(v2_hotels, url_prefix='/api/v2/hotels')
