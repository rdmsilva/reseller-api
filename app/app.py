from flask import Flask

from app.views.auth.auth import auth
from app.views.purchase.purchase import purchase
from app.views.reseller.reseller import reseller


def blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(reseller)
    app.register_blueprint(purchase)


def create_app():
    app = Flask(__name__)
    blueprints(app)
    return app
