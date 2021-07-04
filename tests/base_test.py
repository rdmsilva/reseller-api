from unittest import TestCase

from flask.testing import FlaskClient


class SetUpTestCase(TestCase):
    app: FlaskClient = None

    @classmethod
    def setUpClass(cls) -> None:
        from app.app import create_app
        app = create_app()
        app.config['DEBUG'] = True
        cls.app = app.test_client()
