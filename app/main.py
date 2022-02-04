from fastapi import FastAPI, Response, HTTPException
from app.blog import models
from app.blog.database import engine
from app.blog.routers import blog, user, authentication

models.Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
