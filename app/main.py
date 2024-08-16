from fastapi import FastAPI

from app.routers import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get("/", tags=["root"], summary="receive all objects")
async def root():
    """
    description : Hello world
    you can write anything here ....
    """
    return {"message": "Welcome Back!"}
