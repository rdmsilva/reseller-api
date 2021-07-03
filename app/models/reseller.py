from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import EncryptedType

from app.models.base import BaseModel
from settings import ENCRYPTED_KEY

Base = declarative_base()


class Reseller(Base, BaseModel):
    __tablename__ = 'reseller'

    serialize_only = ('cpf', 'name', 'email')

    cpf = Column(String(11), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(EncryptedType(String, ENCRYPTED_KEY), nullable=False)
