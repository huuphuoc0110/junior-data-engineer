# 🚀 12-Week Data Engineering Roadmap

> A structured 12-week learning journey from Python fundamentals to building production-oriented Data Engineering pipelines.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Advanced-orange?logo=postgresql)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![PySpark](https://img.shields.io/badge/PySpark-Big%20Data-orange?logo=apachespark)
![Airflow](https://img.shields.io/badge/Airflow-Orchestration-red?logo=apacheairflow)
![Kafka](https://img.shields.io/badge/Kafka-Streaming-black?logo=apachekafka)
![dbt](https://img.shields.io/badge/dbt-Analytics%20Engineering-orange?logo=dbt)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue?logo=docker)

---

## 📌 About This Repository

This repository documents my **12-week Data Engineering learning journey**, starting from Python Core & Object-Oriented Programming and progressing toward modern Data Engineering technologies and production-oriented data pipelines.

The roadmap focuses on building both:

- **Strong programming & data fundamentals**
- **Modern Data Engineering skills**
- **Batch & streaming data pipelines**
- **Data transformation & analytics engineering**
- **Data warehouse / lakehouse concepts**
- **Production-oriented projects**

The goal is not only to learn individual tools, but to understand **how the components work together in a real-world Data Engineering ecosystem**.

---

## 🎯 Learning Objectives

By the end of this roadmap, I aim to be able to:

- Write clean, maintainable Python code
- Apply OOP, SOLID and clean code principles
- Work confidently with Git and testing
- Write advanced SQL queries
- Design and optimize relational databases
- Perform data analysis using Pandas & Polars
- Process large datasets with PySpark
- Use DuckDB and Apache Arrow for analytical workloads
- Build batch ETL/ELT pipelines
- Orchestrate workflows using Apache Airflow
- Manage transformations using dbt
- Build streaming pipelines with Apache Kafka
- Understand modern data warehouse architectures
- Work with Snowflake / BigQuery
- Understand Lakehouse architectures
- Implement data quality and testing
- Implement data lineage and observability
- Build production-oriented Data Engineering projects

---

# 🗺️ Roadmap

## Week 1 — Python Core & Basic OOP

**27 lessons · ~40 hours**

Topics:

- Python fundamentals
- Variables & data types
- Control flow
- Functions
- Lists, tuples, sets & dictionaries
- Error handling
- File handling
- Modules & packages
- Type hints
- Basic Object-Oriented Programming
- Classes & objects
- Inheritance
- Encapsulation
- Polymorphism

**Goal:** Build a strong Python foundation for Data Engineering.

---

## Week 2 — Advanced OOP, Async, Clean Code & SOLID

**27 lessons · ~40 hours**

Topics:

- Advanced Object-Oriented Programming
- Abstract classes
- Interfaces / protocols
- Composition
- Decorators
- Context managers
- Iterators & generators
- Async programming
- `asyncio`
- Clean Code
- SOLID principles
- Design principles

**Goal:** Write maintainable and scalable Python applications.

---

## Week 3 — Git, Pytest & Basic SQL

**27 lessons · ~40 hours**

Topics:

### Git

- Git fundamentals
- Branching
- Merging
- Rebasing
- Pull Requests
- Conflict resolution
- Git workflow

### Testing

- Pytest
- Unit testing
- Fixtures
- Mocking
- Test organization

### SQL

- SELECT
- WHERE
- JOIN
- GROUP BY
- HAVING
- Subqueries
- Basic aggregation

**Goal:** Build reliable code and become comfortable working with version control and databases.

---

## Week 4 — Advanced SQL & PostgreSQL

**27 lessons · ~40 hours**

Topics:

- Advanced JOINs
- CTE
- Recursive CTE
- Window Functions
- Query optimization
- Indexes
- Execution plans
- Transactions
- PostgreSQL
- Database design
- Constraints
- Performance tuning

**Goal:** Develop strong SQL and relational database skills.

---

## Week 5 — Pandas & Polars

**27 lessons · ~40 hours**

Topics:

- DataFrames
- Data cleaning
- Data transformation
- Missing values
- Filtering
- Grouping
- Aggregation
- Joins
- Reshaping
- Pandas
- Polars
- Performance comparison

**Goal:** Learn how to manipulate and transform structured datasets efficiently.

---

## Week 6 — PySpark, DuckDB & Apache Arrow

**27 lessons · ~40 hours**

Topics:

### PySpark

- Spark architecture
- DataFrames
- Transformations
- Actions
- Lazy evaluation
- Distributed processing
- Partitioning
- Spark SQL

### DuckDB

- Analytical SQL
- Local OLAP
- Querying files directly
- Parquet

### Apache Arrow

- Columnar data
- Memory-efficient data processing
- Interoperability between data tools

**Goal:** Understand how to process larger datasets efficiently.

---

## Week 7 — Airflow & dbt Fundamentals

**27 lessons · ~40 hours**

Topics:

### Apache Airflow

- DAGs
- Tasks
- Operators
- Scheduling
- Dependencies
- XCom
- Task retries
- Workflow orchestration

### dbt

- Models
- Sources
- Seeds
- Tests
- Documentation
- Basic transformations

**Goal:** Build and orchestrate reproducible data pipelines.

---

## Week 8 — Advanced Airflow, dbt, Dagster & dlt

**27 lessons · ~40 hours**

Topics:

- Advanced Airflow
- Dynamic DAGs
- TaskFlow API
- Sensors
- Scheduling strategies
- Advanced dbt
- Incremental models
- Data quality
- Dagster
- dlt
- Pipeline architecture

**Goal:** Understand different approaches to data pipeline orchestration and ingestion.

---

## Week 9 — Kafka, Streaming & Snowflake / BigQuery

**27 lessons · ~40 hours**

Topics:

### Apache Kafka

- Producers
- Consumers
- Topics
- Partitions
- Consumer groups
- Offsets
- Event-driven architecture

### Streaming

- Real-time data processing
- Streaming pipelines
- Event-based systems

### Cloud Data Warehouse

- Snowflake
- BigQuery
- Data warehouse concepts
- OLAP architecture

**Goal:** Build an understanding of modern batch + streaming architectures.

---

## Week 10 — Delta / Iceberg, Great Expectations & OpenLineage

**27 lessons · ~40 hours**

Topics:

### Lakehouse

- Delta Lake
- Apache Iceberg
- ACID transactions
- Schema evolution
- Time travel
- Data versioning

### Data Quality

- Great Expectations
- Data validation
- Data quality checks
- Expectations

### Data Lineage

- OpenLineage
- Metadata
- Pipeline lineage
- Observability

**Goal:** Understand production-grade data reliability, quality and lineage.

---

# 🏗️ Projects

## Week 11 — Project 1: ELT Pipeline

### Project 1 — ELT Pipeline

Build an end-to-end **ELT data pipeline**.

Expected architecture:

```text
Source
  │
  ▼
Extract
  │
  ▼
Load
  │
  ▼
Data Warehouse
  │
  ▼
Transform
  │
  ▼
Analytics