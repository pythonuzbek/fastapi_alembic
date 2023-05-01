import os

from sqlalchemy.orm import declarative_base,  sessionmaker

from settings import settings
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1@localhost:5432/p8', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
