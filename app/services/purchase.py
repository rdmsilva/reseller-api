from datetime import datetime

from app.models.base import async_session
from app.models.purchase import Purchase

ON_APPROVAL = 'Em validação'
APPROVED = 'Aprovado'
APPROVED_CPF = 15350946056


def save_new_purchase(purchase: Purchase):
    purchase.created_at = datetime.now()
    purchase.status = APPROVED if purchase.cpf == APPROVED_CPF else ON_APPROVAL
    purchase.save()
    return purchase.id


def get_purchase_by_cpf(cpf):
    with async_session() as session:
        return session.query(Purchase).filter_by(cpf=cpf).all()
