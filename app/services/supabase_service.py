from supabase import create_client, Client
from app.core.config import settings

# Server-side Supabase client (FULL ACCESS, bypasses RLS)
service_supabase: Client = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_SERVICE_ROLE_KEY
)

