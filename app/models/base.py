from contextlib import contextmanager
from uuid import UUID

from sqlalchemy import create_engine, Column, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_serializer import SerializerMixin

from log import logger
from settings import DB_URI

database_uri = DB_URI

engine = create_engine(database_uri)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class CustomSerializerMixin(SerializerMixin):
    serialize_types = ((UUID, lambda x: str(x)),)


@contextmanager
def async_session() -> 'Session':
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
    updated_at = Column(DateTime, nullable=True)
    deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)

    def save(self):
        with async_session() as session:
            session.add(self)
        return self

    def delete(self):
        with async_session() as session:
            session.delete(self)
        return self
