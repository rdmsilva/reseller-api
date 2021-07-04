from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

from app.models.base import BaseModel
from settings import ENCRYPTED_KEY

BaseReseller = declarative_base()


class Reseller(BaseReseller, BaseModel):
    __tablename__ = 'reseller'

    serialize_only = ('cpf', 'name', 'email')

    id = Column(Integer, primary_key=True, autoincrement=True)
    cpf = Column(StringEncryptedType(Integer, length=255, key=ENCRYPTED_KEY, engine=AesEngine), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(StringEncryptedType(String, length=255, key=ENCRYPTED_KEY, engine=AesEngine), primary_key=True, nullable=False)
