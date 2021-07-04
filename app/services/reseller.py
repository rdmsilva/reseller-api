from datetime import datetime

from app.models.base import async_session
from app.models.reseller import Reseller


def save_new_reseller(reseller: Reseller):
    reseller.created_at = datetime.now()
    reseller.save()
    return reseller.id


def get_reseller_by_cpf(cpf):
    with async_session() as session:
        return session.query(Reseller).filter_by(cpf=cpf, deleted=False).first()
