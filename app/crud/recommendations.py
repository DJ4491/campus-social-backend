# Placeholder: we will call rec_engine here
from app.services.rec_engine import simple_mutual_rec
from app.services.supabase_service import service_supabase


def get_recommendations_for_user(user_id):

    try:
        data = {}
        response = (
            service_supabase.table("profiles")
            .select("id, created_at, username")
            .order("created_at", desc=True)
            .execute()
        )
        
        friendship_response = (
            service_supabase.table('friendships')
            .select("user_id","friend_id")
            .eq("status","accepted")
            .execute()
        )
        friendship_data = friendship_response.data
        data["users"] = response.data
        
        for user in data["users"]:
            if "friends" not in user:
                user["friends"] = []
            for friend in friendship_data:
                if user["id"] == friend["user_id"]:
                    user["friends"].append(friend["friend_id"])
        
        return simple_mutual_rec(user_id,data)
        # return data
    except Exception as e:
        return f"There was a problem: {e}"

