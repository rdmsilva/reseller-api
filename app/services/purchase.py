from datetime import datetime

from sqlalchemy.exc import IntegrityError

from app.exceptions import CustomException
from app.models.app_models import Purchase
from app.models.base import context_session
from app.schemas.purchase import PurchaseSchema

ON_APPROVAL = 'Em validação'
APPROVED = 'Aprovado'
APPROVED_CPF = 15350946056


def apply_status(purchase: Purchase):
    return APPROVED if purchase.cpf == APPROVED_CPF else ON_APPROVAL


def apply_benefits(purchase: dict):
    purchase_value = purchase['value']
    percent = 0
    cashback = 0

    if purchase_value <= 1000:
        percent = 10
        cashback = purchase_value * (percent / 100)
    elif 1000 < purchase_value <= 1500:
        percent = 15
        cashback = purchase_value * (percent / 100)
    elif purchase_value > 1500:
        percent = 20
        cashback = purchase_value * (percent / 100)

    purchase['percent'] = percent
    purchase['cashback'] = cashback

    return purchase


def save_new_purchase(data: dict):
    try:
        purchase = Purchase(**PurchaseSchema().load(data))
        purchase.created_at = datetime.now()
        purchase.status = apply_status(purchase)
        purchase.save()
    except IntegrityError:
        raise CustomException(msg="CPF not registered for a reseller", status_code=400)

    return purchase.id


def find_all_purchase(cpf):
    with context_session() as session:
        filter_args = []
        if cpf:
            filter_args.append(Purchase.cpf == cpf)

        purchases = session.query(Purchase).filter(*filter_args).all()

        return list(map(lambda _: apply_benefits(_.to_dict()), purchases))


def find_purchase_by_id(purchase_id):
    with context_session() as session:
        return session.query(Purchase).filter_by(id=purchase_id).first()


def update_purchase(actual: Purchase, new_data: dict):
    for k, v in new_data.items():
        actual.__setattr__(k, v)
    actual.save()
    return actual


def delete_purchase(purchase_id):
    with context_session() as session:
        purchase = session.query(Purchase).filter_by(id=purchase_id).first()
        purchase.delete()
