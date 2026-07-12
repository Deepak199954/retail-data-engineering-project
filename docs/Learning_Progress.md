# Project Roadmap

## Vision

This project is designed to simulate a real-world Retail Data Engineering platform rather than a collection of isolated SQL or PySpark examples.

The project will evolve gradually as new business requirements are introduced, just as they would in a production environment.

The primary objective is to understand **why** transformations are required before implementing them using SQL and PySpark.

---

# Current Learning Phase

## Phase 1 — SQL Foundations *(In Progress)*

### Completed

- SQL Fundamentals
- Aggregate Functions
- GROUP BY
- HAVING
- CASE
- INNER JOIN
- LEFT JOIN
- FULL OUTER JOIN
- UNION
- UNION ALL
- Common Table Expressions (CTE)
- Scalar Subqueries
- Multiple-row Subqueries (`IN`)
- Correlated Subqueries
- EXISTS
- ANY / ALL *(Conceptual — Databricks alternative using MIN/MAX discussed)*
- Window Functions
  - Ranking Functions
    - ROW_NUMBER()
    - RANK()
    - DENSE_RANK()
  - Value Functions
    - LAG()
    - LEAD()
    - FIRST_VALUE()
    - LAST_VALUE()
  - Aggregate Window Functions
    - SUM() OVER()
    - AVG() OVER()
    - MIN() OVER()
    - MAX() OVER()
  - Window Frames
    - Default Frame
    - Explicit Frames (`ROWS BETWEEN ...`)

### Upcoming

- CROSS JOIN
- SELF JOIN *(Deferred until the Employees dataset is introduced naturally)*

> **Note 1:** RIGHT JOIN was intentionally skipped after understanding LEFT JOIN thoroughly, as both concepts are logically equivalent by changing the driving table.

> **Note 2:** SELF JOIN has been intentionally deferred instead of introducing artificial columns into the current datasets. It will be learned naturally when the `employees` dataset introduces hierarchical relationships (`employee → manager`).

Business scenarios continue to be presented as Jira tickets so that solutions are driven by business requirements instead of SQL syntax.
# Learning Methodology

Every ticket in this project follows the same workflow:

```text
Jira Ticket
        ↓
Requirement Analysis
        ↓
Business Entity
        ↓
Output Grain
        ↓
Column Ownership
        ↓
Requirement Validation
        ↓
Solution Design
        ↓
SQL
        ↓
GitHub PR Review
        ↓
Production Discussion
        ↓
Spark Execution Discussion
```

The objective is to think like a Data Engineer before writing SQL.

Every solution is reviewed not only for SQL correctness but also for:

- Business logic
- Output grain
- Readability
- Maintainability
- Production suitability
- Alternative approaches

---

# SQL Decision Framework *(Built During Learning)*

Rather than memorizing syntax, SQL concepts are chosen based on business requirements.

```text
Business Requirement
        │
        ▼
Need to combine datasets?
        │
        ▼
JOIN
        │
        ▼
Need business summary?
        │
        ▼
GROUP BY
        │
        ▼
Need to filter aggregated data?
        │
        ▼
HAVING
        │
        ▼
Need conditional business logic?
        │
        ▼
CASE
        │
        ▼
Need an intermediate business result?
        │
        ▼
CTE
        │
        ▼
Need one calculated value?
        │
        ▼
Scalar Subquery
        │
        ▼
Need multiple values?
        │
        ▼
IN (Multiple-row Subquery)
        │
        ▼
Need row-specific calculation?
        │
        ▼
Correlated Subquery
        │
        ▼
Need to check only whether related data exists?
        │
        ▼
EXISTS
        │
        ▼
Need calculations while preserving every row?
        │
        ▼
WINDOW FUNCTIONS
        │
        ├── Need row numbering?
        │       ▼
        │   ROW_NUMBER()
        │
        ├── Need ranking?
        │       ▼
        │   RANK() / DENSE_RANK()
        │
        ├── Need previous / next row?
        │       ▼
        │   LAG() / LEAD()
        │
        ├── Need first / last value?
        │       ▼
        │   FIRST_VALUE() / LAST_VALUE()
        │
        └── Need running or cumulative metrics?
                ▼
        SUM() / AVG() / MIN() / MAX() OVER()
```

This decision framework will continue evolving as new SQL concepts are learned.

---

# Project Development Roadmap

## Phase 2 — Bronze to Silver Pipeline (SQL)

Once SQL concepts are completed, the first production-style pipeline will be built.

```text
Landing
    │
    ▼
Bronze
    │
    ▼
Silver (SQL)
```

The Silver layer will perform transformations such as:

- Data quality validation
- NULL handling
- Data standardization
- Business rule implementation
- Deduplication
- Data enrichment
- Data cleansing

---

## Phase 3 — Silver to Gold Pipeline (SQL)

The cleaned Silver data will be transformed into business-ready Gold tables.

```text
Silver
    │
    ▼
Gold (SQL)
```

Gold tables will support analytics and reporting use cases.

Examples include:

- Customer Sales Summary
- Product Performance
- Category Sales
- City Sales
- Customer Retention
- Inventory Status

---

## Phase 4 — PySpark Implementation

After the SQL pipeline is complete, the exact same business transformations will be implemented using PySpark.

The goal is to learn PySpark by translating already-understood business logic instead of learning business logic and PySpark simultaneously.

Temporary learning tables may be maintained during this phase for comparison and validation.

Example:

```text
silver_orders_sql
silver_orders_pyspark

gold_customer_sales_sql
gold_customer_sales_pyspark
```

Both implementations will be validated to ensure they produce identical business results.

After validation, PySpark will become the production implementation.

---

## Phase 5 — Delta Lake

The project will then be enhanced using Delta Lake features, including:

- MERGE
- UPDATE
- DELETE
- Time Travel
- Optimization
- ACID Transactions

---

## Phase 6 — Production Pipelines

The project will evolve into a production-style solution by adding:

- Incremental processing
- Parameterized notebooks
- Logging
- Audit columns
- Error handling
- Databricks Workflows

---

## Phase 7 — Cloud Integration

Finally, the project will be extended using:

- Azure Data Factory
- Microsoft Fabric

to build an end-to-end cloud-based Retail Data Engineering solution.

---

# Data Model Evolution

The project intentionally starts with only two source tables to simplify learning.

## Current Source Tables

```text
customers
orders
```

Additional datasets will be introduced only when required by realistic business scenarios.

Planned datasets include:

```text
customers
orders
products
stores
payments
inventory
employees
suppliers
```

The project will intentionally evolve from two source tables into a realistic retail data platform instead of introducing all datasets at the beginning.

---

# Learning Philosophy

Every concept in this project follows the same approach:

```text
Business Requirement
        ↓
Requirement Analysis
        ↓
Business Entity
        ↓
Output Grain
        ↓
Column Ownership
        ↓
Business Metric
        ↓
Solution Design
        ↓
SQL
        ↓
PR Review
        ↓
Production Discussion
        ↓
Spark Execution Discussion
        ↓
PySpark
```

The focus is on solving business problems rather than memorizing SQL syntax.

The same business problem is often solved using multiple SQL techniques to understand trade-offs between readability, maintainability, and performance.

---
---

# Window Function Learning Summary

Window Functions were learned using a business-first approach instead of individual syntax.

The progression followed was:

```text
Business Requirement
        ↓
Need to preserve every row?
        ↓
OVER()
        ↓
PARTITION BY
        ↓
ORDER BY
        ↓
WINDOW FRAME
        ↓
Choose the appropriate function
```

Covered categories include:

- Ranking Functions
- Value Functions
- Aggregate Window Functions
- Default Window Frames
- Explicit Window Frames

Every Window Function solution concluded with:

- GitHub PR Review
- Production discussion
- Spark execution discussion
- Comparison with alternative SQL approaches

# Project Goal

By the end of this project, the repository will contain:

- Realistic Retail datasets
- Bronze, Silver, and Gold architecture
- SQL implementations
- PySpark implementations
- Delta Lake features
- Production-style pipelines
- Databricks Workflows
- Azure Data Factory integration
- Microsoft Fabric integration

The outcome will be a complete, interview-ready Retail Data Engineering project built incrementally from first principles.

The emphasis throughout the project is not simply learning SQL syntax, but developing the ability to analyze business requirements, evaluate multiple technical solutions, and choose the most appropriate implementation from both an interview and production perspective.