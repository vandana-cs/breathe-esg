Here is your final README content ready to paste into `README.md`.

# Breathe ESG Tech Intern Assignment

Full-stack ESG emissions ingestion and analyst review system built using Django REST Framework and React.

## Tech Stack

### Backend

* Django
* Django REST Framework
* SQLite
* Gunicorn

### Frontend

* React
* Vite

### Deployment

* Backend: Render
* Frontend: Vercel

---

# Features

* SAP fuel and procurement CSV ingestion
* Utility electricity CSV ingestion
* Travel data sync endpoint
* Emissions normalization
* Analyst approval workflow
* REST APIs
* Audit-friendly raw payload storage

---

# Live Links

Frontend:
[https://breathe-esg-ebon-theta.vercel.app/](https://breathe-esg-ebon-theta.vercel.app/)

Backend API:
[https://breathe-esg-lvrb.onrender.com/api/records/](https://breathe-esg-lvrb.onrender.com/api/records/)

Admin Panel:
[https://breathe-esg-lvrb.onrender.com/admin/](https://breathe-esg-lvrb.onrender.com/admin/)

---

# API Endpoints

## Get Records

```bash
GET /api/records/
```

## Upload SAP CSV

```bash
POST /api/upload/sap/
```

## Upload Utility CSV

```bash
POST /api/upload/utility/
```

## Travel Sync

```bash
POST /api/travel/sync/
```

## Approve Record

```bash
POST /api/approve/<id>/
```

---

# Local Setup

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```bash
http://localhost:5173
```

---

# Project Structure

```bash
breathe-esg/
│
├── backend/
│   ├── config/
│   ├── emissions/
│   ├── manage.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── MODEL.md
├── DECISIONS.md
├── TRADEOFFS.md
├── SOURCES.md
└── README.md
```

---

# Assumptions

* SAP ingestion uses realistic CSV exports instead of direct ERP integration.
* Utility data is uploaded as CSV exports from utility portals.
* Travel sync simulates corporate travel platform ingestion.
* SQLite is used for simplicity in prototype deployment.

---

# Future Improvements

* PostgreSQL database
* Background ingestion jobs with Celery
* PDF utility bill parsing
* Real SAP OData integration
* Authentication and role-based access
* Emission factor libraries
* Anomaly detection for suspicious records

---

# Author

Vandana C S
