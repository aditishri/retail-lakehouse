# Retail Lakehouse

A real-time data engineering project that simulates retail order events and processes them through a Medallion Architecture (Bronze → Silver → Gold) using Apache Kafka and Apache Spark Structured Streaming.

---

## Overview

This project demonstrates an end-to-end streaming data pipeline commonly used in modern data platforms. Retail order events are generated continuously, published to Kafka, processed by Spark Structured Streaming, and transformed into analytics-ready datasets following the Medallion Architecture.

---

## Architecture

```
                  +-------------------+
                  | Order Generator   |
                  +---------+---------+
                            |
                            v
                    +---------------+
                    | Apache Kafka  |
                    +-------+-------+
                            |
                            v
          +---------------------------------+
          | Spark Structured Streaming      |
          +---------------+-----------------+
                          |
          +---------------+----------------+
          |                                |
          v                                v

     Bronze Layer                  Raw Event Storage
 (Raw Kafka Messages)

          |
          v

     Silver Layer
 (Schema Enforcement &
 Data Transformation)

          |
          v

      Gold Layer
 (Business Aggregations)
```

---

## Tech Stack

- Python
- Apache Kafka
- Apache Spark 3.5
- PySpark
- Spark Structured Streaming
- Docker & Docker Compose
- Parquet
- Faker

---

## Features

- Real-time retail order generation
- Kafka-based event streaming
- Spark Structured Streaming pipeline
- Bronze, Silver, and Gold Medallion Architecture
- JSON parsing with explicit schema
- Business metric aggregation
- Dockerized deployment

---

## Project Structure

```
retail-lakehouse/
│
├── producer/
│   ├── app.py
│   ├── transaction_generator.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── spark/
│   ├── bronze_stream.py
│   ├── silver_stream.py
│   ├── silver_transform.py
│   └── gold_aggregation.py
│
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Pipeline

### Bronze Layer

- Reads events from Kafka
- Stores raw events in Parquet format
- Maintains streaming checkpoints

### Silver Layer

- Reads Bronze data
- Parses JSON payloads
- Applies explicit schema
- Produces clean structured datasets

### Gold Layer

Generates business metrics such as:

- Total Orders
- Total Revenue
- Average Order Value
- Order Status Summary

---

## Sample Output

| Status | Total Orders | Total Revenue (Cents) | Average Order Value (Cents) |
|--------|-------------:|----------------------:|----------------------------:|
| placed | 835 | 10,114,668,463 | 12,113,375 |
| cancelled | 24 | 328,231,543 | 13,676,314 |

---

## Skills Demonstrated

- Apache Kafka
- Apache Spark
- Spark Structured Streaming
- ETL Pipeline Development
- Medallion Architecture
- Data Transformation
- Docker Containerization
- Real-time Data Processing

---

## Future Enhancements

- Delta Lake
- Airflow Orchestration
- Data Quality Validation
- Partitioned Tables
- Power BI Dashboard
- CI/CD Pipeline

---

## Author

**Aditi Shrivastava**

GitHub: https://github.com/aditishri