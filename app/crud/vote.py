from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.vote import Vote as VoteModel

def create_vote(db: Session, feature_id: int) -> VoteModel:
    vote = VoteModel(feature_id=feature_id)
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote

def count_votes(db: Session, feature_id: int) -> int:
    return db.query(func.count(VoteModel.id)).filter(VoteModel.feature_id == feature_id).scalar() or 0
