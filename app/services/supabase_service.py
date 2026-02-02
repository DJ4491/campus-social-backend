import os
from supabase import create_client
from app.core.config import settings

# Trusted server-side client (service role key) for admin actions
service_supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_ROLE_KEY)

# Helper: optionally return headers for forwarding a user JWT to Supabase REST
def auth_headers_from_token(user_jwt: str) -> dict:
    return {"Authorization": f"Bearer {user_jwt}", "apikey": settings.SUPABASE_ANON_KEY}
