from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from app.models.base import BaseModel

Base = declarative_base()


class Reseller(Base, BaseModel):
    __tablename__ = 'reseller'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(11), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)
