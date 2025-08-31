# Feature Voting System

A simple FastAPI project where users can post features and upvote them.  
Includes a backend API, SQLite/MySQL database support, and a basic HTML frontend for testing.

---

## Features

- Users can create new features.
- Users can upvote features.
- API endpoints provide vote counts.
- Local HTML page to create/list features and vote.
- Unit tests covering CRUD and endpoints.

---

## Folder Structure

FastAPIProject/

│
├─ app/
│ ├─ main.py
│ ├─ models/
│ │ ├─ feature.py
│ │ └─ vote.py
│ ├─ schemas/
│ │ ├─ feature.py
│ │ └─ vote.py
│ ├─ crud/
│ │ ├─ feature.py
│ │ └─ vote.py
│ ├─ api/
│ │ ├─ endpoints/
│ │ │ ├─ features.py
│ │ │ └─ votes.py
│ │ └─ deps.py
│ └─ tests/
│ └─ test_app.py
└─ static/
└─ index.html

yaml
Copy code

---

## Dependencies

Install required Python packages:

```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic pytest pytest-asyncio
Optional (for local HTML testing):

bash
pip install requests
Database
Example MySQL connection:

bash
mysql+pymysql://user:password@localhost:3306/products_db
Tables are auto-created by SQLAlchemy (Feature and Vote).

For tests, an in-memory SQLite database is used.

Run the Project
Start the FastAPI server:

bash
uvicorn app.main:app --reload
Visit the API docs:

http://127.0.0.1:8000/docs
Test with local HTML:
open static/index.html in your browser

API Endpoints
GET /api/features/ – List all features with vote counts
POST /api/features/ – Create a new feature
POST /api/votes/{feature_id} – Upvote a feature
GET /api/votes/{feature_id} – Get total votes for a feature

CORS Notes
If you test from a local HTML page (different origin):
Make sure CORS is enabled in main.py:

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for local testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Running Unit Tests

pytest app/tests/test_app.py -v
Tests cover:

CRUD for Feature
CRUD for Vote

API endpoints
Uses in-memory SQLite for isolation.
