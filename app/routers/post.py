from fastapi import APIRouter

from app.models.post import UserPost, UserPostIn

router = APIRouter()
post_table = {}


@router.post("/")
async def create_post(post: UserPostIn) -> UserPost:
    data = post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@router.get("/")
async def get_all_posts() -> list[UserPost]:
    return list(post_table.values())
