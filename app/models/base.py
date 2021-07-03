from contextlib import contextmanager

from sqlalchemy import create_engine, Column, DateTime, Boolean
from sqlalchemy.orm import sessionmaker, scoped_session

database_uri = "mysql+pymysql://dev:dev@localhost/reseller-db"

engine = create_engine(database_uri)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


@contextmanager
def async_session() -> 'Session':
    session = Session()
    try:
        yield session
        session.commit()
    except Exception as e:
        # logger.error(e)
        session.rollback()
        raise
    finally:
        session.close()


class BaseModel:
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
