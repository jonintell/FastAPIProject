from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud.feature import get_feature
from app.crud.vote import create_vote, count_votes
from app.schemas.vote import Vote as VoteSchema

router = APIRouter()

# POST /api/votes/{feature_id} -> upvote a feature
@router.post("/{feature_id}", response_model=VoteSchema)
def upvote_feature(feature_id: int, db: Session = Depends(get_db)):
    feature = get_feature(db, feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    vote = create_vote(db, feature_id)
    return VoteSchema(id=vote.id, feature_id=vote.feature_id)

# GET /api/votes/{feature_id} -> get total votes
@router.get("/{feature_id}")
def get_feature_votes(feature_id: int, db: Session = Depends(get_db)):
    feature = get_feature(db, feature_id)
    if not feature:
        raise HTTPException(status_code=404, detail="Feature not found")
    return {"feature_id": feature_id, "votes": count_votes(db, feature_id)}
