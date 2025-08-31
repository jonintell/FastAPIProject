from fastapi import FastAPI
from app.core.database import Base, engine
# Import models to register tables
from app.models import feature as feature_model  # noqa: F401
from app.models import vote as vote_model        # noqa: F401
from app.api.endpoints import features, votes

# Create tables (simple replacement for Spring's ddl-auto=update for this demo)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feature Voting API", version="1.0.0")

# Routers
app.include_router(features.router, prefix="/api/features", tags=["features"])
app.include_router(votes.router,    prefix="/api/features", tags=["votes"])
