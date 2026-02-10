from typing import Union
from app.routes import health, recommendations, admin, posts
from fastapi import FastAPI
app = FastAPI(title="Campus Social Backend", version="0.1.0")

app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])




