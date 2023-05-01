from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class Book(Base):
    __tablename__ = 'books'
    id =  Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)