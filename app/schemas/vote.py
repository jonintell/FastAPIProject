from pydantic import BaseModel

class Vote(BaseModel):
    id: int
    feature_id: int

    class Config:
        orm_mode = True
