from fastapi import FastAPI

from app.models.post import UserPost, UserPostIn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


post_table = {}


@app.post("/post/")
async def create_post(post: UserPostIn) -> UserPost:
    data = post.dict()
    last_record_id = len(post_table)
    new_post = {**data, "id": last_record_id}
    post_table[last_record_id] = new_post
    return new_post


@app.get("/post/")
async def get_all_posts() -> list[UserPost]:
    return list(post_table.values())
