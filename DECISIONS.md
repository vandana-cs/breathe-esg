# Design Decisions

## 1. Why CSV ingestion?
Most enterprise clients export SAP and utility data as CSV rather than direct API access.

---

## 2. Why mock Travel data?
Real APIs (Concur/Navan) require authentication. For prototype, static structure is used.

---

## 3. Why single table model?
To simplify normalization and make analytics easier.

---

## 4. Why Django REST?
Fast backend development and built-in admin panel.

---

## 5. Why React?
Simple UI for analysts to review and approve emissions data.

---

## 6. What was assumed?
- Emission factors are simplified
- No authentication system
- No real SAP API integration