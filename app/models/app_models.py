from sqlalchemy import Column, String, Integer, Float, Date, Index, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

from app.models.base import BaseModel
from settings import ENCRYPTED_KEY

Base = declarative_base()


class Reseller(Base, BaseModel):
    __tablename__ = 'reseller'

    serialize_only = ('cpf', 'name', 'email')

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(StringEncryptedType(Integer, length=255, key=ENCRYPTED_KEY, engine=AesEngine), nullable=False,
                 unique=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(StringEncryptedType(String, length=255, key=ENCRYPTED_KEY, engine=AesEngine), nullable=False)

    purchases = relationship('Purchase', backref='reseller')


class Purchase(Base, BaseModel):
    __tablename__ = 'purchase'

    serialize_only = ('code', 'value', 'date', 'status')

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String(15), nullable=False)

    cpf = Column(StringEncryptedType(Integer, length=255, key=ENCRYPTED_KEY, engine=AesEngine), ForeignKey('reseller.cpf'), nullable=False)


index_cpf = Index('idx_purchase_cpf', Purchase.cpf)
