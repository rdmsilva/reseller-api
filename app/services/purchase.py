from datetime import datetime

from app.models.base import context_session
from app.models.purchase import Purchase

ON_APPROVAL = 'Em validação'
APPROVED = 'Aprovado'
APPROVED_CPF = 15350946056


def save_new_purchase(purchase):
    purchase.created_at = datetime.now()
    purchase.status = APPROVED if purchase.cpf == APPROVED_CPF else ON_APPROVAL
    purchase.save()
    return purchase.id


def get_purchase_by_cpf(cpf):
    with context_session() as session:
        return session.query(Purchase).filter_by(cpf=cpf).all()


def get_purchase_by_id(id):
    with context_session() as session:
        return session.query(Purchase).filter_by(id=id).first()


def update_purchase(actual, data):
    for k, v in data.items():
        actual.__setattr__(k, v)
    actual.save()
    return actual
