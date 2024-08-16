from fastapi import FastAPI

from app.routers.blog_get import router

app = FastAPI()
app.include_router(router)


@app.get("/", tags=["root"], summary="receive all objects")
async def root():
    """
    description : Hello world
    you can write anything here ....
    """
    return {"message": "Welcome Back!"}
