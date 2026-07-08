# 🛒 Retail Data Engineering Project

## 📌 Project Overview

This project demonstrates an end-to-end Retail Data Engineering pipeline built using Databricks, PySpark, SQL, Delta Lake, Azure, and Microsoft Fabric.

The objective is to simulate a real-world retail environment where customer and order data is ingested, transformed through the Medallion Architecture (Bronze, Silver, Gold), and prepared for analytics and reporting.

---

## 🏗️ Architecture

Landing (CSV Files)
        │
        ▼
Bronze (Raw Delta Tables)
        │
        ▼
Silver (Cleaned & Standardized Data)
        │
        ▼
Gold (Business Aggregations)
        │
        ▼
Reporting / Analytics

---

## 🛠️ Technology Stack

- Databricks
- Apache Spark (PySpark)
- Spark SQL
- Delta Lake
- Unity Catalog
- Azure Data Lake Storage (ADLS)
- Git & GitHub
- Microsoft Fabric (Upcoming)

---

## 📂 Project Structure

```
retail-data-engineering-project/
│
├── README.md
├── .gitignore
├── data/
│   └── raw/
│       ├── customers.csv
│       └── orders.csv
│
├── src/
│   ├── generate_customers.py
│   └── generate_orders.py
│
├── notebooks/
│   └── bronze_ingestion.py
│
├── docs/
├── azure/
├── fabric/
└── workflows/
```

---

# 🚀 Project Progress

| Ticket | Task | Status |
|---------|------|--------|
| DE-001 | Generate Retail Datasets | ✅ Completed |
| DE-002 | Landing & Bronze Ingestion | ✅ Completed |
| DE-003 | Silver Layer Transformations | ⏳ In Progress |
| DE-004 | Gold Layer Business Aggregations | ⏳ Pending |
| DE-005 | Delta Lake Features | ⏳ Pending |
| DE-006 | Databricks Workflows | ⏳ Pending |
| DE-007 | Azure Implementation | ⏳ Pending |
| DE-008 | Microsoft Fabric Implementation | ⏳ Pending |

---

# ✅ Completed So Far

- Generated Customers dataset using Python
- Generated Orders dataset using Python
- Uploaded datasets to Databricks Volume (Landing)
- Created Bronze Delta Tables
- Ingested data into Bronze using PySpark
- Initialized Git repository
- Published project to GitHub

---

# 📅 Next Milestone

- Create Silver Layer
- Learn Spark SQL
- Clean and standardize Bronze data
- Build production-ready Silver tables

---

## 👨‍💻 Author

**Deepak**

This project is being built as part of my journey toward becoming a Data Engineer, focusing on Databricks, Apache Spark, Azure, and Microsoft Fabric.