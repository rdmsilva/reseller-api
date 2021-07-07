from base64 import b64encode
from http import HTTPStatus
from json import loads
from unittest.mock import patch

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from tests.base_test import BaseApiTestCase


class LoginTest(BaseApiTestCase):
    login_route = '/v1/auth'

    @patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock())
    def test_401_login(self, mock_session):
        credentials = b64encode(' :123456'.encode()).decode()
        response = self.client.post(self.login_route, headers={'Authorization': f'Basic {credentials}'})
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_400_login(self):
        credentials = b64encode('12312312323'.encode()).decode()
        response = self.client.post(self.login_route, headers={'Authorization': f'Basic {credentials}'})
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_200_login(self):
        data = {"name": "Rafael Revendedor",
                        "email": "rafael.revendedor@hotmail.com",
                        "cpf": "12312312323",
                        "password": "123456"}

        self.client.post('/v1/resellers', json={'data': data}, headers=self.headers)

        credentials = b64encode('12312312323:123456'.encode()).decode()
        response = self.client.post(self.login_route, headers={'Authorization': f'Basic {credentials}'})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('token', loads(response.data).keys())
