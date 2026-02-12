from fastapi import APIRouter
from app.crud.recommendations import get_recommendations_for_user
from fastapi import Depends
from app.deps.auth import get_current_user

router = APIRouter()


@router.get("/", summary="Mutual Friends")
async def get_mutual_friends(): #current_user = Depends(get_current_user)
    user_id = "00000000-0000-0000-0000-000000000001"
    return get_recommendations_for_user(user_id)
