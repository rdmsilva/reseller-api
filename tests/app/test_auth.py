from http import HTTPStatus
from unittest.mock import patch

from mock_alchemy.mocking import UnifiedAlchemyMagicMock

from tests.base_test import SetUpTestCase


class LoginTest(SetUpTestCase):
    login_route = '/v1/auth'

    @patch('app.models.base.Session', return_value=UnifiedAlchemyMagicMock())
    def test_login(self, session):
        with self.app as client:
            response = client.get(self.login_route)
            self.assertEqual(response.status_code, HTTPStatus.OK)
