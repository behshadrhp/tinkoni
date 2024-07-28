from random import randrange
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool
    rating: Optional[int] = None


my_posts = [
    {
        "id": 1,
        "title": "Hello world",
        "content": "How are you?",
        "published": True,
        "raging": 4,
    },
    {
        "id": 2,
        "title": "Can You Help me ?",
        "content": "Yes I can :)",
        "published": False,
        "rating": 1,
    },
    {
        "id": 3,
        "title": "Can i do it ?",
        "content": "Yes I can :)",
        "published": True,
        "rating": 4,
    },
]


def find_post(id):
    """
    This class is for find post with id.
    """
    for post in my_posts:
        if post["id"] == id:
            return post


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/posts/")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts/")
async def create_posts(post: Post):
    # added id to post
    post_instance = post.dict()
    post_instance["id"] = randrange(0, 100000000000)

    # added to my posts
    my_posts.append(post_instance)

    return {"data": post}


@app.get("/posts/{id}/")
async def get_posts(id: int):

    post = find_post(id)
    return {"detail": post}
