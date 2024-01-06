from fastapi import FastAPI
from typing import Optional  # noqa
from db.models import Base  # noqa
from db import models
from db.database import engine
from router import user
from router import blog_get
from router import blog_post

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/hello")
def index():
    return {"message": "Hello world!"}


models.Base.metadata.create_all(engine)
