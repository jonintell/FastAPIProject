from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.models import feature as feature_model  # noqa
from app.models import vote as vote_model        # noqa
from app.api.endpoints import features, votes

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feature Voting API", version="1.0.0")

# -------------------
# CORS setup
# -------------------
origins = [
    "http://localhost:63344",  # PyCharm preview
    "http://127.0.0.1:63344",  # sometimes different host
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # or ["*"] for all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, etc.
    allow_headers=["*"],        # Content-Type, Authorization, etc.
)

# Routers
app.include_router(features.router, prefix="/api/features", tags=["features"])
app.include_router(votes.router,    prefix="/api/votes", tags=["votes"])
