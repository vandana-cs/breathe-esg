# Data Source Research

## 1. SAP Data
Real-world SAP exports are typically:
- CSV / Excel extracts
- IDoc structured data
- OData APIs

For this prototype:
- Simplified to CSV upload
- Assumed columns: fuel_type, quantity, unit, date

---

## 2. Utility Data
Typically comes from:
- Electricity provider portals
- Monthly billing CSV or PDF

For prototype:
- Used CSV with kWh and billing period

---

## 3. Travel Data (Concur/Navan-like)
Real systems provide:
- Flight segments
- Airport codes
- Distances sometimes missing

For prototype:
- Mocked structured JSON with distance in km