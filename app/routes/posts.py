# app/routes/posts.py
from fastapi import APIRouter
from app.crud.posts import create_post_db

router = APIRouter()


@router.get("/", summary="Posts")
async def get_posts():
    # create_post_db is sync; calling it directly is fine.
    # If create_post_db becomes async you can await it instead.
    return create_post_db()
