from sqlalchemy.orm import Session
from app.models.feature import Feature as FeatureModel
from app.schemas.feature import FeatureCreate

def get_features(db: Session) -> list[FeatureModel]:
    return db.query(FeatureModel).all()

def get_feature(db: Session, feature_id: int) -> FeatureModel | None:
    return db.query(FeatureModel).filter(FeatureModel.id == feature_id).first()

def create_feature(db: Session, feature: FeatureCreate) -> FeatureModel:
    db_feature = FeatureModel(title=feature.title, description=feature.description)
    db.add(db_feature)
    db.commit()
    db.refresh(db_feature)
    return db_feature
