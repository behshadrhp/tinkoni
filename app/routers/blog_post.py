from fastapi import APIRouter

router = APIRouter(prefix="/blog", tags=["blog"])


@router.post("/create/")
async def post_blog():
    pass
