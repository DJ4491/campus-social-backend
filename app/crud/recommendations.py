# Placeholder: we will call rec_engine here
from app.services.rec_engine import simple_mutual_rec

def get_recommendations_for_user(user_id: str):
    return simple_mutual_rec(user_id)
