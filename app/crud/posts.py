# app/crud/posts.py
from app.services.supabase_service import service_supabase


def create_post_db(limit: int, offset: int):

    start = offset
    end = offset + limit - 1

    resp = (
        service_supabase.table("posts")
        .select(
            "id,created_at,title,desc,image,likes,author_id,"
            + "author:profiles!posts_author_id_fkey(id,username,display_name,avatar_url)"
        )
        .order("created_at", desc=True)
        .range(start,end)
        .execute()
    )

    # resp is a PostgrestResponse object; .data is a Python list/dict
    return resp.data
