
from flask import Blueprint
from flask import Flask
# from app.api.v1.routes.hotels import hotels_bp
# from app.swagger.app import v1_swagger_bp

def register_api(app):
    from .v1.routes.hotels import hotels_bp as v1_hotels
    # from .v2.routes.hotels import hotels_bp as v2_hotels
    from .v1.routes.swagger import swagger_bp as v1_swagger_bp

    app.register_blueprint(v1_hotels, url_prefix='/api/v1/hotels')
    app.register_blueprint(v1_swagger_bp, url_prefix='/api/v1/swagger')

