from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, token
from .. hashing import Hash

def login(db: Session, request: models.User):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if user is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'User not found')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Invalid username or password')
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
