# ETL Automation in Google Cloud with Data Fusion, Airflow, and BigQuery

This repository demonstrates an Extract, Transform, Load (ETL) process leveraging Google Cloud technologies, including Data Fusion, BigQuery, and Cloud Composer (Apache Airflow). The pipeline automates data workflows from extraction to visualization.

---

## Project Overview

This project implements an ETL pipeline that:

1. **Extracts data**: A Python script generates employee data and saves it as a CSV file.
2. **Stores data in Google Cloud Storage (GCS)**: The generated file is uploaded to a GCS bucket.
3. **Transforms and loads data using Data Fusion**: A Cloud Data Fusion pipeline applies transformations and loads the data into BigQuery.
4. **Loads transformed data into BigQuery**: The pipeline integrates processed data into BigQuery tables.
5. **Visualizes the data**: Dashboards are created in Looker for insights.
6. **Automates with Airflow**: The pipeline is orchestrated using Apache Airflow within Cloud Composer.

---

## Repository Structure

- **`extract.py`**: Python script to generate employee data, store it locally, and upload it to GCS.
- **`dag.py`**: Airflow DAG script for orchestrating the pipeline, including task dependencies and schedule settings.

---

## Workflow Details

### 1. Data Extraction
The `extract.py` script uses the Faker library to generate fake employee data with the following fields:
- First Name
- Last Name
- Job Title
- Department
- Email
- Address
- Phone Number
- Salary
- Password 

The data is saved as `employee_data.csv` and uploaded to a specified GCS bucket.

### 2. Data Storage
The CSV file is uploaded to GCS using the `google-cloud-storage` library.

- **GCS Bucket Name**: `employee-data-bckt`
- **File Path**: `employee_data.csv`

### 3. Data Transformation and Loading
A Cloud Data Fusion pipeline performs the following:
- Masks sensitive data (e.g., passwords).
- Encodes data for secure storage.
- Loads the transformed data into BigQuery.

### 4. BigQuery Integration
The processed data is stored in BigQuery tables, enabling structured queries and downstream analysis.

### 5. Data Visualization
Looker dashboards provide visual insights into the loaded data, helping stakeholders derive actionable insights.

### 6. Workflow Automation
Airflow automates the entire ETL process:
- **`extract_data`**: Executes the `extract.py` script.
- **`start_datafusion_pipeline`**: Triggers the Data Fusion pipeline.

---

## Airflow Configuration

### DAG Settings
- **DAG Name**: `employee_data`
- **Schedule Interval**: `@daily`
- **Retries**: 1 (5-minute retry delay)

### DAG Tasks
1. **`extract_data`**: Runs the `extract.py` script.
2. **`start_datafusion_pipeline`**: Starts the Data Fusion pipeline using the `CloudDataFusionStartPipelineOperator`.

---

## Requirements

### Python Libraries
- `faker`
- `google-cloud-storage`
- `apache-airflow`

### Google Cloud Components
- **Cloud Composer**: To manage Airflow.
- **Cloud Data Fusion**: For ETL transformations.
- **BigQuery**: To store and query data.
- **Looker**: For data visualization.

---


## Visualization in Looker
Create dashboards to visualize employee salary distributions, departmental breakdowns, and other insights.

