from datetime import datetime
from http import HTTPStatus
from unittest.mock import patch

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from tests.base_test import SetUpTestCase


class PurchaseTest(SetUpTestCase):
    reseller_route = '/v1/purchase'

    default_data = {"code": "boti123",
                    "value": 120.50,
                    "date": datetime.now().date().isoformat(),
                    'cpf': '12345678900'}

    @patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock())
    def test_new_purchase(self, session):
        with self.app as client:
            response = client.post(self.reseller_route, json={'data': self.default_data})
            self.assertEqual(response.status_code, HTTPStatus.CREATED)
