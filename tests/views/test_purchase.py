from datetime import datetime
from http import HTTPStatus

from tests.base_test import BaseApiTestCase


class PurchaseApiTest(BaseApiTestCase):
    purchases_route = '/v1/purchases'

    default_data = {"code": "b123456", "value": 120.50, "date": datetime.now().date().isoformat(),
                    'cpf': '12345678900'}

    def test_400_missing_cpf(self):
        response = self.client.post(self.purchases_route, json={'data': self.default_data.copy().pop('cpf')},
                                    headers=self.headers)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_401_missing_token(self):
        response = self.client.post(self.purchases_route, json={'data': self.default_data})
        self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

    def test_new_purchase(self):
        response = self.client.post(self.purchases_route, json={'data': self.default_data}, headers=self.headers)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
