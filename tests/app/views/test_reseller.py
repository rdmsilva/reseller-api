from http import HTTPStatus
from random import randint

from tests.base_test import BaseApiTestCase


class ResellerTest(BaseApiTestCase):
    reseller_route = '/v1/resellers'

    default_data = {"name": "Rafael Revendedor",
                    "email": "rafael.revendedor@hotmail.com",
                    "cpf": "12345678900",
                    "password": "123"}

    def test_201_new_reseller(self):
        data = self.default_data.copy()
        data['cpf'] = ''.join([str(randint(0, 11)) for _ in range(0, 12)])
        response = self.client.post(self.reseller_route, json={'data': data})
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_400_new_reseller(self):
        data = self.default_data.copy()
        data['cpf'] = ''.join([str(randint(0, 11)) for _ in range(0, 12)])
        data.pop('email')
        response = self.client.post(self.reseller_route, json={'data': data})
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

        response = self.client.post(self.reseller_route)
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test_400_amount_cashback(self):
        response = self.client.post(self.reseller_route, json={'data': self.default_data})
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

        response = self.client.get(f'{self.reseller_route}/1/cashback', headers=self.headers)
        self.assertEqual(response.status_code, HTTPStatus.OK)
