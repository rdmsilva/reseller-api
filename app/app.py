from flask import Flask

from app.views.reseller import reseller


def register_blueprint(app):
    app.register_blueprint(reseller)


def create_app():
    app = Flask(__name__)
    register_blueprint(app)
    return app
