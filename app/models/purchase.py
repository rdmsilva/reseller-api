from sqlalchemy import Column, String, Integer, Float, Date
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import StringEncryptedType

from app.models.base import BaseModel
from settings import ENCRYPTED_KEY

Base = declarative_base()


class Purchase(Base, BaseModel):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(30), nullable=False)
    value = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    cpf = Column(StringEncryptedType(String, ENCRYPTED_KEY), primary_key=True, nullable=False)
    status = Column(String(15), nullable=False)
