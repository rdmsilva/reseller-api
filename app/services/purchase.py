from datetime import datetime
from http import HTTPStatus

from app.exceptions import CustomException
from flask import jsonify
from sqlalchemy.exc import IntegrityError

from app.models.app_models import Purchase
from app.models.base import context_session
from app.schemas.purchase import PurchaseSchema
from app.services.reseller import get_reseller_by_cpf

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
    purchase['cashback'] = round(cashback, 2)

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


def find_all_purchases(reseller_cpf):
    reseller = get_reseller_by_cpf(reseller_cpf)
    return list(map(lambda _: apply_benefits(_.to_dict()), reseller.purchases))


def find_purchase_by_id(purchase_id):
    with context_session() as session:
        return session.query(Purchase).filter_by(id=purchase_id).first()


def validated_auth_cpf(auth_cpf, current_cpf):
    if auth_cpf != current_cpf:
        return jsonify(msg='purchase cpf must be the same that reseller'), HTTPStatus.UNAUTHORIZED


def update_purchase(new_data: dict, auth_cpf: int):
    if validated_auth_cpf(auth_cpf, int(new_data['cpf'])):
        return jsonify(msg='purchase cpf must be the same that reseller'), HTTPStatus.UNAUTHORIZED

    status = new_data.get('status')
    if status and status not in [APPROVED, ON_APPROVAL]:
        return jsonify(msg='status not allowed'), HTTPStatus.BAD_REQUEST

    actual = find_purchase_by_id(int(new_data['id']))

    if not actual:
        return jsonify(msg='purchase not found'), HTTPStatus.BAD_REQUEST

    if actual.status == APPROVED:
        return jsonify(msg='purchase is already approved'), HTTPStatus.BAD_REQUEST

    for k, v in new_data.items():
        actual.__setattr__(k, v)

    actual.save()

    return jsonify(actual.to_dict()), HTTPStatus.OK


def delete_purchase(purchase_id, auth_cpf):
    with context_session() as session:
        purchase = session.query(Purchase).filter_by(id=purchase_id).first()

        if not purchase:
            return jsonify(msg='purchase not found'), HTTPStatus.BAD_REQUEST

        if not purchase.cpf == auth_cpf:
            return jsonify(msg='purchase cpf must be the same that reseller'), HTTPStatus.UNAUTHORIZED

        purchase.delete()
        return jsonify(msg='purchase deleted'), HTTPStatus.OK
