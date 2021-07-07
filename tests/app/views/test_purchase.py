from datetime import datetime
from http import HTTPStatus
from json import loads

from app.services.purchase import ON_APPROVAL, APPROVED_CPF, APPROVED
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

        response = self.client.get(f'{self.purchases_route}/1', headers=self.headers)
        self.assertEqual(loads(response.data)['status'], ON_APPROVAL)

        aproved_data = self.default_data.copy()
        aproved_data['cpf'] = APPROVED_CPF
        aproved_data['code'] = 'b1111'
        response = self.client.post(self.purchases_route, json={'data': aproved_data}, headers=self.headers)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        response = self.client.get(self.purchases_route, headers=self.headers)
        self.assertIn(APPROVED, list(map(lambda x: x['status'], loads(response.data))))
