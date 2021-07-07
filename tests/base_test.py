from unittest import TestCase
from unittest.mock import patch

from flask.testing import FlaskClient
from flask_jwt_extended import create_access_token
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


class BaseApiTestCase(TestCase):
    app: FlaskClient = None

    @classmethod
    def setUpClass(cls) -> None:
        from app.app import create_app
        app = create_app()
        app.config['TESTING'] = True
        app.config['DEBUG'] = True

        with app.test_request_context():
            token = create_access_token(identity="test", expires_delta=False)
            cls.headers = {
                'Authorization': f'Bearer {token}'
            }

        cls.client = app.test_client()

        patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock()).start()

    def setUp(self) -> None:
        print(self._testMethodName)
