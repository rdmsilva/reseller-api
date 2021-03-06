from contextlib import contextmanager
from uuid import UUID

from sqlalchemy import create_engine, Column, DateTime
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_serializer import SerializerMixin

from log import logger
from settings import DB_URI

engine = create_engine(DB_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class CustomSerializerMixin(SerializerMixin):
    serialize_types = ((UUID, lambda x: str(x)),)


@contextmanager
def context_session() -> 'Session':
    session = Session()
    try:
        yield session
        session.commit()
        session.flush()
    except Exception as e:
        logger.error(e)
        session.rollback()
        raise


class BaseModel(CustomSerializerMixin):
    created_at = Column(DateTime, nullable=False)

    def save(self):
        with context_session() as session:
            session.add(self)
        return self

    def delete(self):
        with context_session() as session:
            session.delete(self)
        return self
