FlexiMart Data Architecture Project



Student Name: Tejaswini Sahu

Student ID: BITSOM-BA-25071667

Email: tejaswiniblog@gmail.com

Date: 08-01-2026



Project Overview



This project builds a complete data system for FlexiMart, an e-commerce company. It starts by cleaning raw CSV data and loading it into a relational database. Business analysis is then performed using SQL queries.



The project also designs a NoSQL product catalog and creates a data warehouse using a star schema for analytical reporting. Overall, it demonstrates the full data lifecycle, from data preparation to advanced analytics.



Repository Structure

├── data/

│   ├── customers\_raw.csv

│   ├── products\_raw.csv

│   └── sales\_raw.csv

│

├── part1-database-etl/

│   ├── README.md

│   ├── etl\_pipeline.py

│   ├── schema\_documentation.md

│   ├── business\_queries.sql

│   ├── data\_quality\_report.txt

│   └── requirements.txt

│

├── part2-nosql/

│   ├── README.md

│   ├── nosql\_analysis.md

│   ├── mongodb\_operations.js

│   └── products\_catalog.json

│

└── part3-datawarehouse/

&nbsp;   ├── README.md

&nbsp;   ├── star\_schema\_design.md

&nbsp;   ├── warehouse\_schema.sql

&nbsp;   ├── warehouse\_data.sql

&nbsp;   └── analytics\_queries.sql



Technologies Used



Python 3.x,pandas,mysql-connector-python

Relational Database:MySQL 8.0 / PostgreSQL 14,NoSQL Database,MongoDB 6.0



Concepts

ETL (Extract-Transform-Load)

Data Cleaning \& Quality Reporting

OLTP vs OLAP

Star Schema \& Dimensional Modeling

Aggregations \& Window Functions

NoSQL Document Modeling



Setup Instructions

1\) Database Setup (MySQL / PostgreSQL)

\# Create databases

mysql -u root -p -e "CREATE DATABASE fleximart;"

mysql -u root -p -e "CREATE DATABASE fleximart\_dw;"



2\) Run Part 1 – ETL Pipeline

python part1-database-etl/etl\_pipeline.py



3\) Execute Business Queries

mysql -u root -p fleximart < part1-database-etl/business\_queries.sql



4\) Run Data Warehouse Scripts

\# Create schema

mysql -u root -p fleximart\_dw < part3-datawarehouse/warehouse\_schema.sql



\# Load sample data

mysql -u root -p fleximart\_dw < part3-datawarehouse/warehouse\_data.sql



\# Run OLAP analytical queries

mysql -u root -p fleximart\_dw < part3-datawarehouse/analytics\_queries.sql



MongoDB Setup

mongosh < part2-nosql/mongodb\_operations.js





Key Learnings



Learned the difference between OLTP systems and data warehouses



Built ETL workflows for data cleaning, transformation, and loading



Used SQL features such as joins, aggregations, CTEs, and window functions



Designed a star schema suitable for analytical reporting



Challenges Faced



Dirty and incomplete data

Cleaned the data using Python and pandas by removing duplicates, fixing date formats, handling missing values, and correcting data types.



Foreign key insertion errors

Solved this by loading dimension tables first and the fact table afterward to maintain referential integrity.



Star schema design decisions

Used a clear rule: one row per product per order, which prevented double counting and simplified reporting.



