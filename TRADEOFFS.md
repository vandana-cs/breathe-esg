# Tradeoffs

## 1. No SAP direct integration
Instead of IDoc/OData, we used CSV upload for simplicity.

---

## 2. No PDF parsing
Utility bills assumed as CSV, not real PDFs.

---

## 3. No authentication system
Skipped login system to focus on ingestion and review logic.

---

## 4. No scalable data warehouse
Used SQLite instead of PostgreSQL for speed.

---

## 5. No background jobs
Processing is synchronous instead of queue-based (Celery).