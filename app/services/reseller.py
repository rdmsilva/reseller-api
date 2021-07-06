import hashlib
from datetime import datetime

from app.models.base import context_session
from app.models.reseller import Reseller
from settings import SALT


def save_new_reseller(reseller: Reseller):
    reseller.password = generate_hash_password(reseller.password)
    reseller.created_at = datetime.now()
    reseller.save()
    return reseller.id


def get_reseller_by_id(id):
    with context_session() as session:
        return session.query(Reseller).filter_by(id=id).first()


def get_reseller_by_cpf(cpf):
    with context_session() as session:
        return session.query(Reseller).filter_by(cpf=cpf).first()


def generate_hash_password(password):
    return hashlib.md5(f'{password}-{SALT}'.encode()).hexdigest()


def password_is_valid(password, uer):
    return uer.password == generate_hash_password(password)
