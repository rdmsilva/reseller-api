from sqlalchemy import Column, String, Integer, Float, Date, Index
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

from app.models.base import BaseModel
from settings import ENCRYPTED_KEY

BasePurchase = declarative_base()


class Purchase(BasePurchase, BaseModel):
    __tablename__ = 'purchase'

    serialize_only = ('code', 'value', 'date', 'status')

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    cpf = Column(StringEncryptedType(Integer, length=255, key=ENCRYPTED_KEY, engine=AesEngine), nullable=False)
    status = Column(String(15), nullable=False)


index_cpf = Index('idx_purchase_cpf', Purchase.cpf)
