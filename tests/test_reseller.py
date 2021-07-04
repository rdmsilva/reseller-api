from http import HTTPStatus
from random import randint
from unittest.mock import patch

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from tests.base_test import SetUpTestCase


class BasicTests(SetUpTestCase):
    reseller_route = '/v1/reseller'

    default_data = {"name": "Rafael Dantas",
                    "email": "rdmsilva@hotmail.com",
                    "cpf": "12345678900",
                    "password": "123"}

    @patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock())
    def test_new_reseller_created(self, session):
        with self.app as client:
            data = self.default_data.copy()
            data['cpf'] = ''.join([str(randint(0, 11)) for _ in range(0, 12)])
            response = client.post(self.reseller_route, json={'data': data})
            self.assertEqual(response.status_code, HTTPStatus.CREATED)

    @patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock())
    def test_get_reseller(self, session):
        with self.app as client:
            session.query.return_value.filter.return_value = None
            response = client.get(f'{self.reseller_route}/1111111111')
            self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    @patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock())
    def test_new_reseller_bad_request(self, session):
        with self.app as client:
            data = self.default_data.copy()
            data.pop('password')
            response = client.post(self.reseller_route, json={'data': data})
            self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
