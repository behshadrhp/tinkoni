from fastapi import APIRouter, Query
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    comments: int
    published: bool = False


@router.post("/create/{id}")
async def post_blog(blog: BlogModel, id: int, version: int = 1):

    return {"id": id, "version": version, "data": blog}


@router.post("/create/{id}/comment")
async def comment_blog(blog: BlogModel, id: int, comment_id: int = Query(None)):
    return {"id": id, "comment_id": comment_id, "blog": blog}
