# Placeholder: we will call rec_engine here
from app.services.rec_engine import simple_mutual_rec
from app.services.supabase_service import service_supabase

def get_recommendations_for_user():
    response = (
        service_supabase.table("posts")
        .select("id, created_at, author, avatar, title, image, desc, likes")
        .order("created_at", desc=True)
        .execute()
    )
    return response.data

    return simple_mutual_rec(user_id)
