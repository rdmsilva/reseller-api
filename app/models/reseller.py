from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base

from app.models.base import BaseModel

Base = declarative_base()


class Reseller(Base, BaseModel):
    __tablename__ = 'reseller'

    cpf = Column(String(11), primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)
