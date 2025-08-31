Feature Voting API (FastAPI + MySQL)

Simple API that allows users to post features and upvote others. This project includes a backend API, database integration, and a minimal HTML frontend for testing.

Features

Post new features (title + optional description)

List all features with current vote counts

Upvote existing features

View vote count per feature

Technology Stack

Backend: FastAPI

Database: MySQL (via SQLAlchemy ORM)

Frontend: Basic HTML + JS (fetch API)

Python Version: 3.11+

Dependencies: see requirements.txt

Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd FastAPIProject

2. Create MySQL Database
CREATE DATABASE products_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'user';
GRANT ALL PRIVILEGES ON products_db.* TO 'user'@'localhost';
FLUSH PRIVILEGES;


You can change the username/password in app/core/config.py or via the DATABASE_URL environment variable.

3. Install Python dependencies
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

4. Run the backend
uvicorn app.main:app --reload


The backend will start at:

http://127.0.0.1:8000

5. Open Swagger UI (API docs)

Visit:

http://127.0.0.1:8000/docs


Test all endpoints here

Check feature creation, voting, and vote counts

6. Test with HTML frontend

Open index.html in your browser (or serve it via PyCharm)

Add features

Upvote features

See vote counts update in real time

If you see a CORS error, make sure CORSMiddleware is enabled in app/main.py.

API Endpoints
Endpoint	Method	Description
/api/features/	POST	Create a new feature
/api/features/	GET	List all features with vote counts
/api/votes/{feature_id}	POST	Upvote a feature
/api/votes/{feature_id}	GET	Get total votes for a feature
Notes

No authentication is implemented for simplicity

Database tables are auto-created on startup

CORSMiddleware allows frontend access from different origins (dev only)