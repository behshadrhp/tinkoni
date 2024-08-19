from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


class BlogModel(BaseModel):
    title: str
    content: str
    comments: int
    published: bool = False


@router.post("/create/")
async def post_blog(blog: BlogModel):

    return {"data": blog}
