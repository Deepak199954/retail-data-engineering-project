# Project Roadmap

## Vision

This project is designed to simulate a real-world Retail Data Engineering platform rather than a collection of isolated SQL or PySpark examples.

The project will evolve gradually as new business requirements are introduced, just as they would in a production environment.

The primary objective is to understand **why** transformations are required before implementing them using SQL and PySpark.

---

# Current Learning Phase

## Phase 1 — SQL Foundations *(In Progress)*

### Completed

* SQL Fundamentals
* Aggregate Functions
* GROUP BY
* HAVING
* CASE
* INNER JOIN
* LEFT JOIN

### Upcoming

* RIGHT JOIN
* FULL OUTER JOIN
* SELF JOIN
* CROSS JOIN
* UNION
* UNION ALL
* CTE
* Subqueries
* Correlated Subqueries
* Window Functions

Business scenarios are presented as Jira tickets so that solutions are driven by business requirements instead of SQL syntax.

---

# Project Development Roadmap

## Phase 2 — Bronze to Silver Pipeline (SQL)

Once SQL concepts are completed, the first production-style pipeline will be built.

```
Landing
    │
    ▼
Bronze
    │
    ▼
Silver (SQL)
```

The Silver layer will perform transformations such as:

* Data quality validation
* NULL handling
* Data standardization
* Business rule implementation
* Deduplication
* Data enrichment
* Data cleansing

---

## Phase 3 — Silver to Gold Pipeline (SQL)

The cleaned Silver data will be transformed into business-ready Gold tables.

```
Silver
    │
    ▼
Gold (SQL)
```

Gold tables will support analytics and reporting use cases.

Examples include:

* Customer Sales Summary
* Product Performance
* Category Sales
* City Sales
* Customer Retention
* Inventory Status

---

## Phase 4 — PySpark Implementation

After the SQL pipeline is complete, the exact same business transformations will be implemented using PySpark.

The goal is to learn PySpark by translating already-understood business logic instead of learning business logic and PySpark simultaneously.

Temporary learning tables may be maintained during this phase for comparison and validation.

Example:

```
silver_orders_sql
silver_orders_pyspark

gold_customer_sales_sql
gold_customer_sales_pyspark
```

Both implementations will be validated to ensure they produce identical business results.

After validation, PySpark will be treated as the production implementation.

---

## Phase 5 — Delta Lake

The project will then be enhanced using Delta Lake features, including:

* MERGE
* UPDATE
* DELETE
* Time Travel
* Optimization
* ACID Transactions

---

## Phase 6 — Production Pipelines

The project will evolve into a production-style solution by adding:

* Incremental processing
* Parameterized notebooks
* Logging
* Audit columns
* Error handling
* Databricks Workflows

---

## Phase 7 — Cloud Integration

Finally, the project will be extended using:

* Azure Data Factory
* Microsoft Fabric

to build an end-to-end cloud-based Retail Data Engineering solution.

---

# Data Model Evolution

The project intentionally starts with only two source tables to simplify learning.

## Current Source Tables

```
customers
orders
```

As business requirements grow, additional source systems will be introduced.

Planned datasets include:

```
customers
orders
products
stores
payments
inventory
employees
suppliers
```

New datasets will only be introduced when required by a realistic business scenario.

---

# Learning Philosophy

Every concept in this project follows the same approach:

```
Business Requirement
        ↓
Business Metric
        ↓
Expected Output
        ↓
Solution Design
        ↓
SQL
        ↓
PySpark
        ↓
Production Pipeline
```

The focus is on solving business problems rather than memorizing syntax.

---

# Project Goal

By the end of this project, the repository will contain:

* Realistic Retail datasets
* Bronze, Silver, and Gold architecture
* SQL implementations
* PySpark implementations
* Delta Lake features
* Production-style pipelines
* Databricks Workflows
* Azure Data Factory integration
* Microsoft Fabric integration

The outcome will be a complete, interview-ready Retail Data Engineering project built incrementally from first principles.
