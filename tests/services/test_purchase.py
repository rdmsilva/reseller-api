from unittest import TestCase

from app.models.app_models import Purchase
from app.services.purchase import apply_benefits, apply_status, ON_APPROVAL, APPROVED, APPROVED_CPF


class PurchaseServiceTest(TestCase):

    def setUp(self) -> None:
        print(self._testMethodName)

    def test_apply_benefits_ten_percent(self):
        purchases = [{'value': 800}, {'value': 1000}, {'value': 100}, {'value': 999}]

        purchases_cashback = list(map(lambda _: apply_benefits(_), purchases))

        for purchase in purchases_cashback:
            self.assertEqual(purchase['percent'], 10)
            self.assertEqual(purchase['cashback'], purchase['value'] * (purchase['percent'] / 100))

    def test_apply_benefits_fifth_percent(self):
        purchases = [{'value': 1001}, {'value': 1500}, {'value': 1300}, {'value': 1250}]

        purchases_cashback = list(map(lambda _: apply_benefits(_), purchases))

        for purchase in purchases_cashback:
            self.assertEqual(purchase['percent'], 15)
            self.assertEqual(purchase['cashback'], purchase['value'] * (purchase['percent'] / 100))

    def test_apply_benefits_twenty_percent(self):
        purchases = [{'value': 1501}, {'value': 2000}, {'value': 10000}, {'value': 20000}]

        purchases_cashback = list(map(lambda _: apply_benefits(_), purchases))

        for purchase in purchases_cashback:
            self.assertEqual(purchase['percent'], 20)
            self.assertEqual(purchase['cashback'], purchase['value'] * (purchase['percent'] / 100))

    def test_apply_status_on_approval(self):
        self.assertEqual(ON_APPROVAL, apply_status(Purchase(cpf=12345678900)))

    def test_apply_status_approved(self):
        self.assertEqual(APPROVED, apply_status(Purchase(cpf=APPROVED_CPF)))
