from random import randrange
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
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
    This function is for find post with id.
    """
    for post in my_posts:
        if post["id"] == id:
            return post


def find_index(id):
    """
    This function is for find index post with id.
    """

    for index, post in enumerate(my_posts):
        if post["id"] == id:
            return index


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/posts/")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts/", status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    # added id to post
    post_instance = post.dict()
    post_instance["id"] = randrange(0, 100000000000)

    # added to my posts
    my_posts.append(post_instance)

    return {"data": post}


@app.get("/posts/{id}/")
async def get_posts(id: int, response: Response):

    post = find_post(id)

    # response handel
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not Found :)",
        )

    return {"detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):

    # delete object from db
    index = find_index(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not Found :)",
        )

    my_posts.pop(index)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}", status_code=status.HTTP_201_CREATED)
async def update_post(id: int, post: Post):

    # update object from db
    index = find_index(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not Found :)",
        )

    # apply changes
    post_instance = post.dict()
    post_instance["id"] = id
    my_posts[index] = post_instance

    return {"data": post_instance}
