from enum import Enum
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome Back!"}


@app.get("/blog/all/")
async def get_blog(page: int = 1, page_size: Optional[int] = 2):
    return {"message": f"all {page_size} of blog on pages {page}"}


@app.get("/blog/{id}/comment/{comment_id}/")
async def get_comment(id: int, comment_id: int, username: Optional[str] = None):
    return {"message": f"blog_id: {id}, comment_id: {comment_id}, username: {username}"}


class BlogType(str, Enum):
    short = "short"
    long = "long"
    pain = "pain"


@app.get("/blog/type/{type}")
async def get_blog_type(type: BlogType):
    return {"message": f"blog type is {type}"}


@app.get("/blog/post/{id}")
async def get_post(id: int):
    return {"message": f"blog post is {id}"}
