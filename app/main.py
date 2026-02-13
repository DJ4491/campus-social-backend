from typing import Union
from app.routes import health, mutual_friend, recommendations, admin,posts_you_may_like,posts
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Campus Social Backend", version="0.1.0")
origins = ["http://localhost:8081"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(health.router, prefix="/health", tags=["health"])
app.include_router(posts.router, prefix="/posts", tags=["Posts"])
app.include_router(
    recommendations.router, prefix="/recommendations", tags=["recommendations"]
)
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(mutual_friend.router, prefix="/api/mutual_friends", tags=["Mutual Friend"])
app.include_router(posts_you_may_like.router, prefix="/api/posts_you_may_like", tags=["Posts Recommendation"])
