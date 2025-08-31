from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.core.database import Base

class Feature(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(String(500))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    votes = relationship(
        "Vote",
        back_populates="feature",
        cascade="all, delete-orphan"
    )
