from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models

def list_blog(db: Session):
    blog = db.query(models.Blog).all()
    return blog

def create_blog(request: models.Blog, db: Session):
    new_blog = models.Blog(title = request.title, body= request.body, user_id=request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def get_blog(db: Session, id: int):
    blog = db.query(models.Blog).get(id)
    if blog is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Blog not found')
    return blog

def delete_blog(db: Session, id: int):
    blog = db.query(models.Blog).get(id)
    if blog is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Blog not found')
    db.delete(blog)
    db.commit()
    return 'blog deleted'

def update_blog(db: Session, id: int, request: models.Blog):
    blog = db.query(models.Blog).get(id)
    if blog is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Blog not found')
    blog.title = request.title
    blog.body = request.body
    db.commit()
    return 'blog updated'