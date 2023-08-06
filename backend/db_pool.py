from models import Base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///coffee_machines.db"


def create_tables():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)


def get_db_session():
    engine = create_engine(DATABASE_URL)
    session_factory = sessionmaker(bind=engine)
    return session_factory()


if __name__ == "__main__":
    create_tables()

