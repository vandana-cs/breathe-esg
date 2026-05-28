# Data Model (Breathe ESG Prototype)

## Overview
This system stores emissions data from multiple enterprise sources (SAP, Utility, Travel) and normalizes them into a single unified schema for analysis and audit review.

---

## Core Table: EmissionRecord

| Field | Type | Purpose |
|------|------|---------|
| source | string | Data origin (SAP / UTILITY / TRAVEL) |
| activity_type | string | Type of activity (fuel, electricity, flight) |
| quantity | float | Raw input value (liters / kWh / km) |
| unit | string | Unit of measurement |
| record_date | date | Date of activity |
| emissions | float | Normalized CO₂ estimate |
| suspicious | boolean | Flag for anomaly detection |
| review_status | string | PENDING / APPROVED |
| raw_data | JSON | Original source payload |

---

## Multi-Source Normalization Strategy

All sources are converted into a single emission format:
CO₂ = quantity × emission_factor

Example factors:
- Diesel: 2.5
- Electricity: 0.8
- Flight: 0.15

---

## Multi-Tenancy (Simplified)
Not fully implemented, but designed for:
- Adding `client_id` field per record in future

---

## Audit Trail Design
Each record contains:
- raw_data (original unmodified input)
- review_status (approval tracking)

Future improvement:
- add created_by, updated_at, audit_logs table