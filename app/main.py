from enum import Enum
from typing import Optional

from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/", tags=["root"], summary="receive all objects")
async def root():
    """
    description : Hello world
    you can write anything here ....
    """
    return {"message": "Welcome Back!"}


@app.get("/blog/all/", tags=["blog"])
async def get_blog(page: int = 1, page_size: Optional[int] = 2):
    return {"message": f"all {page_size} of blog on pages {page}"}


@app.get("/blog/{id}/comment/{comment_id}/", tags=["blog"])
async def get_comment(id: int, comment_id: int, username: Optional[str] = None):
    return {"message": f"blog_id: {id}, comment_id: {comment_id}, username: {username}"}


class BlogType(str, Enum):
    short = "short"
    long = "long"
    pain = "pain"


@app.get("/blog/type/{type}", tags=["blog"])
async def get_blog_type(type: BlogType):
    return {"message": f"blog type is {type}"}


@app.get("/blog/post/{id}", tags=["blog"])
async def get_post(id: int):
    return {"message": f"blog post is {id}"}


@app.get("/blog/range/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
async def get_blog_range(id: int, response: Response):

    if id < 10:
        response.status_code = status.HTTP_200_OK
        return {"success": "found post :)"}
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Not Found post"}
