from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class FeatureBase(BaseModel):
    title: str
    description: Optional[str] = None

class FeatureCreate(FeatureBase):
    pass

class Feature(FeatureBase):
    id: int
    created_at: datetime
    votes: int = 0

    class Config:
        orm_mode = True
