from fastapi import APIRouter, Depends, Request
from fastapi.routing import APIRoute
from sqlalchemy.orm import Session

import models
from database import get_db
from models import Book

api = APIRouter()


@api.get('/books/')
async def all_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@api.post('/books/')
async def add_books(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    print(data)
    user = models.Book(title=data['title'], author=data['author'])
    db.add(user)
    db.commit()
    return 'succes ⭐ ⭐ ⭐'
