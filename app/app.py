from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager

from app.views.auth import auth
from app.views.purchases import purchase
from app.views.resellers import reseller
from settings import JWT_SECRET_KEY


def config_jwt(app):
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)
    JWTManager(app)


def resgister_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(reseller)
    app.register_blueprint(purchase)


def create_app():
    app = Flask(__name__)
    resgister_blueprints(app)
    config_jwt(app)
    return app
