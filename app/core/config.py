from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SUPABASE_URL: str
    SUPABASE_SERVICE_ROLE_KEY: str
    SUPABASE_ANON_KEY: str | None = None
    JWKS_URL: str
    AUDIENCE: str = "authenticated"
    ISSUER: str

    class Config:
        env_file = ".env"

settings = Settings()
