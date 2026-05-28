# Breathe ESG Tech Intern Assignment

Full-stack ESG emissions ingestion and analyst review system.

## Tech Stack

- Backend: Django REST Framework
- Frontend: React + Vite
- Database: SQLite
- Deployment:
  - Backend: Render
  - Frontend: Vercel

## Features

- SAP fuel/procurement CSV ingestion
- Utility electricity ingestion
- Travel data ingestion
- Emissions normalization
- Approval workflow
- Analyst dashboard
- REST APIs

## Live Links

Frontend:
PASTE_YOUR_VERCEL_URL

Backend:
https://breathe-esg-lvrb.onrender.com/api/records/

## Run Locally

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```
