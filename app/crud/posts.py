from app.services.supabase_service import service_supabase
from typing import Dict, Any


def create_post_db(post: Dict[str, Any]):
    # post contains keys: user_id, content, image_path
    res = service_supabase.table("posts").insert(post).execute()
    return res.data
