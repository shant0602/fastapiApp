from fastapi import FastAPI
from typing import Optional  # noqa
from db.models import Base  # noqa
from db import models
from db.database import engine
from router import user
from router import blog_get
from router import blog_post
from router import article
from router import file
from auth import authentication
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(authentication.router)
app.include_router(file.router)


@app.get("/hello")
def index():
    return {"Message": "Hello world!"}


models.Base.metadata.create_all(engine)

app.mount("/files", StaticFiles(directory="files"), name="files")
