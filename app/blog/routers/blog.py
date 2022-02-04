from curses import def_shell_mode
from lib2to3.pgen2.pgen import DFAState
from signal import SIG_DFL
from this import d
from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database, oauth2
from ..repository import blog

router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/', response_model=List[schemas.ShowBlog], status_code=status.HTTP_200_OK)
def list_blog(db: Session = Depends(database.get_db),  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.list_blog(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.ShowBlog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create_blog(db, request)

@router.get('/{id}', response_model=schemas.ShowBlog, status_code=status.HTTP_200_OK)
def get_blog(id, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_blog(db, id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.delete_blog(db, id)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update_blog(db, id, request)