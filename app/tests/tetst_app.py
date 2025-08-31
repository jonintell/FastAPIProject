import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.models.feature import Base as FeatureBase
from app.models.vote import Base as VoteBase
from app.schemas.feature import FeatureCreate
from app.crud.feature import create_feature
from app.crud.vote import create_vote, count_votes

# -------------------------------
# Setup in-memory DB for testing
# -------------------------------
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
FeatureBase.metadata.create_all(bind=engine)
VoteBase.metadata.create_all(bind=engine)


@pytest.fixture()
def db():
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture()
def client():
    return TestClient(app)


# -------------------------------
# Unit Tests
# -------------------------------

def test_create_and_get_feature(db):
    feature_in = FeatureCreate(title="Test Feature", description="Just a test")
    feature = create_feature(db, feature_in)

    assert feature.id is not None
    assert feature.title == "Test Feature"


def test_create_vote_and_count(db):
    # create a feature first
    feature_in = FeatureCreate(title="Vote Feature")
    feature = create_feature(db, feature_in)

    # add votes
    create_vote(db, feature.id)
    create_vote(db, feature.id)

    votes_count = count_votes(db, feature.id)
    assert votes_count == 2


def test_api_create_and_list_features(client):
    # create feature via API
    response = client.post("/api/features/", json={"title": "API Feature", "description": "via API"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "API Feature"
    assert "votes" in data

    # list features
    response = client.get("/api/features/")
    assert response.status_code == 200
    features = response.json()
    assert any(f["title"] == "API Feature" for f in features)


def test_api_vote_feature(client):
    # create feature
    response = client.post("/api/features/", json={"title": "Vote API"})
    feature_id = response.json()["id"]

    # vote via API
    vote_resp = client.post(f"/api/votes/{feature_id}")
    assert vote_resp.status_code == 200
    assert vote_resp.json()["feature_id"] == feature_id

    # check vote count
    count_resp = client.get(f"/api/votes/{feature_id}")
    assert count_resp.status_code == 200
    assert count_resp.json()["votes"] == 1
