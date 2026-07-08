# Bronze Layer Notes

## What is Bronze Layer?

Bronze is the first layer of the Medallion Architecture.

Its responsibility is to ingest raw data exactly as received from the source systems.

The Bronze layer should preserve the original data as much as possible.

---

## Data Flow

Source System
        │
        ▼
Landing (CSV Files)
        │
        ▼
Bronze (Delta Tables)

---

## Why do we have a Landing Area?

Landing stores the original files received from external systems.

Examples:

- customers.csv
- orders.csv

The Landing area acts as a backup of the source data.

If Bronze tables are accidentally deleted, they can be rebuilt from the Landing files.

---

## Why not read directly from source systems?

Reasons:

- Reliability
- Replay capability
- Auditability
- Decouples source systems from analytics

---

## Bronze Characteristics

- Raw data
- Minimal transformations
- Preserve original values
- Mostly append-only
- Stored as Delta Tables

---

## Why Delta instead of CSV?

CSV

- Plain text
- No metadata
- No schema enforcement
- No ACID transactions

Delta

- Stores data as Parquet
- Maintains _delta_log
- ACID compliant
- Supports Time Travel
- Supports Schema Enforcement
- Supports Schema Evolution

---

## Delta Table Internals

A Delta Table consists of:

Table
│
├── Parquet Files
└── _delta_log

Parquet stores the actual data.

_delta_log stores metadata and transaction history.

---

## Catalog vs Schema vs Table

Catalog

Highest-level container.

Example:

retailcorp

↓

Schema

Logical grouping of tables.

Examples:

bronze
silver
gold

↓

Table

Stores business data.

Example:

customers
orders

---

## Volume

A Volume stores files.

Examples:

customers.csv
orders.csv

Volumes are used for Landing.

Tables are created from those files.

---

## Managed Table

Spark manages:

- Metadata
- Storage
- Delta Log

Dropping the table deletes both metadata and data.

---

## External Table

Spark manages only metadata.

Actual files remain in cloud storage.

Dropping the table removes only metadata.

---

## Reading CSV

```python
spark.read \
    .format("csv") \
    .option("header", True) \
    .option("inferSchema", True) \
    .load("/Volumes/retailcorp/ingestion/landing/customers.csv")
```

header=True

Uses the first row as column names.

inferSchema=True

Spark attempts to determine column data types.

---

## Writing Delta Table

```python
df.write \
  .format("delta") \
  .mode("overwrite") \
  .saveAsTable("retailcorp.bronze.customers")
```

---

## save() vs saveAsTable()

save()

Writes Delta files to a storage path.

Example:

```python
df.write.save("/Volumes/bronze/customers")
```

Read again using:

```python
spark.read.format("delta").load(path)
```

saveAsTable()

Registers the data as a Unity Catalog table.

Example:

```python
df.write.saveAsTable("retailcorp.bronze.customers")
```

Read using SQL:

```sql
SELECT * FROM retailcorp.bronze.customers;
```

---

## Write Modes

overwrite

Replace existing data.

append

Add new data.

ignore

Skip write if destination exists.

error

Fail if destination already exists.

---

## Bronze Pipeline

customers.csv
        │
        ▼
Landing Volume
        │
        ▼
Spark DataFrame
        │
        ▼
Delta Table
        │
        ▼
Bronze Layer

---

## GitHub Milestone

Completed:

- Generate datasets
- Upload to Landing
- Bronze ingestion
- Bronze validation

Ticket:

DE-002 Completed

---

## Interview Questions

Q. Why do we need a Landing Area?

A.

Landing preserves original source files so Bronze tables can be rebuilt.

---

Q. Why use Delta instead of CSV?

A.

Delta provides ACID transactions, schema enforcement, metadata, and time travel.

---

Q. Difference between save() and saveAsTable()?

A.

save() writes to storage.

saveAsTable() writes and registers a table in Unity Catalog.

---

Q. Why is Bronze mostly append-only?

A.

Bronze preserves historical raw data exactly as received from source systems.