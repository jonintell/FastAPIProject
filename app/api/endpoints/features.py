from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud.feature import create_feature as create_feature_crud, get_features
from app.schemas.feature import Feature as FeatureSchema, FeatureCreate
from app.crud.vote import count_votes

router = APIRouter()

@router.post("/", response_model=FeatureSchema)
def create_feature(feature: FeatureCreate, db: Session = Depends(get_db)):
    created = create_feature_crud(db, feature)
    # include computed votes in response
    return FeatureSchema(
        id=created.id,
        title=created.title,
        description=created.description,
        created_at=created.created_at,
        votes=0,
    )

@router.get("/", response_model=List[FeatureSchema])
def list_features(db: Session = Depends(get_db)):
    features = get_features(db)
    # Compute vote counts (simple and clear)
    return [
        FeatureSchema(
            id=f.id,
            title=f.title,
            description=f.description,
            created_at=f.created_at,
            votes=count_votes(db, f.id)
        )
        for f in features
    ]
