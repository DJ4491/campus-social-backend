from fastapi import APIRouter
from app.crud.recommendations import get_recommendations_for_user

router = APIRouter()


@router.get("/", summary="Posts")
async def get_posts():
    return get_recommendations_for_user()
