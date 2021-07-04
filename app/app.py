from flask import Flask

from app.views.auth.auth import auth
from app.views.reseller.reseller import reseller


def blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(reseller)


def create_app():
    app = Flask(__name__)
    blueprints(app)
    return app
