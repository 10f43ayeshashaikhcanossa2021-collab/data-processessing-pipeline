# Generic Data Processing Pipeline

A Python-based data processing pipeline that reads raw data from CSV, JSON, or API sources, validates and cleans the data, handles missing values and data type issues, performs generic transformations, and produces structured output.

The pipeline is designed to be **generalized and dataset-independent**. The current sample dataset is customer data, but the pipeline does not depend on customer-specific columns and can be reused with other tabular datasets.
## Features
* CSV data ingestion
* JSON data ingestion
* REST API data ingestion
* Generic data validation
* Automatic column name standardization
* Missing value handling
* Duplicate record removal
* Automatic numeric type detection
* Automatic date detection
* Text cleaning
* Empty row removal
* Empty column removal
* Generic data transformation
* Data quality reporting
* Configurable input and output paths
* Logging
* Exception handling
* Automated testing
* Structured output generation

## Technologies Used
* **Python**
* **Pandas**
* **Requests**
* **Pytest**
* **JSON**
* **Git & GitHub**
  
## Project Architecture
```text
                         Raw Data
                            |
              +-------------+-------------+
              |             |             |
             CSV           JSON          API
              |             |             |
              +-------------+-------------+
                            |
                            v
                    Data Ingestion
                            |
                            v
                    Data Validation
                            |
                            v
                    Type Detection
                            |
                            v
                     Data Cleaning
                            |
              +-------------+-------------+
              |             |             |
        Missing Values   Duplicates   Invalid Data
              |             |             |
              +-------------+-------------+
                            |
                            v
                    Transformation
                            |
                            v
                    Quality Report
                            |
                            v
                   Structured Output
                            |
                       CSV / JSON
                            |
                            v
                        Logging
```
# Project Structure

```text
data-processing-pipeline/
│
├── data/
│   ├── input/
│   │   └── customers.csv
│   │
│   └── output/
│       └── cleaned_data.csv
│
├── config/
│   └── config.json
│
├── logs/
│   └── pipeline.log
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── ingestion.py
│   ├── validation.py
│   ├── cleaning.py
│   ├── transformation.py
│   └── logger.py
│
├── tests/
│   └── test_pipeline.py
│
├── .gitignore
├── requirements.txt
└── README.md
```
---
# How the Pipeline Work
The pipeline processes raw data through multiple stages.
## 1. Data Ingestion
The ingestion module reads data from different sources.
Supported sources:
* CSV files
* JSON files
* REST APIs
The input source is specified through the configuration file.
Example:
```text
data/input/customers.csv
```

## 2. Data Validation

Before processing, the pipeline checks whether the input dataset is valid.
It verifies that:
* The input exists
* The dataset is not empty
* The dataset contains columns
* The data can be loaded successfully
The validation is generic and does not require fixed column names.

## 3. Column Standardization
Column names are automatically standardized.
For example:
```text
"Customer Name"
" Email "
"Phone Number"
```
becomes:
```text
customer_name
email
phone_number
```
This provides consistent column naming throughout the pipeline.
---
## 4. Data Cleaning
The pipeline performs generic cleaning operations.
### Empty rows
Completely empty rows are removed.
### Empty columns
Columns containing no values are removed.
### Duplicate records
Duplicate rows are detected and removed.
### Text cleaning
Leading and trailing spaces are removed from text values.
Example:

```text
" Ayesha "
```
becomes:
```text
"Ayesha"
```
## 5. Data Type Detection
The pipeline attempts to automatically identify appropriate data types.
### Numeric values
Columns containing mostly numeric values are converted to numeric data types.
For example:
```text
20
21
22
25
```
can be converted from text to numeric values.
### Date values
Date-like columns are automatically detected and converted into datetime values.
---
## 6. Missing Value Handling
Missing values are handled based on the detected column type.
### Numeric columns
Missing numeric values are replaced with the column median when a valid median is available.
### Text columns
Missing text values are replaced with:
```text
Unknown
```
### Date columns
Missing dates are preserved rather than assigning an artificial date.
---
# Sample Dataset
The current sample dataset is:
```text
customers.csv
```
It contains customer-related information and is used to demonstrate the pipeline.

Example:
```csv
customer_id,name,email,age,city,phone
101,Ayesha,ayesha@gmail.com,20,Mumbai,9876543210
102,Rahul,rahul@gmail.com,21,Pune,9876543211
103,,sana@gmail.com,22,Mumbai,9876543212
104,Ali,ali@gmail.com,abc,Delhi,9876543213
105,Neha,neha@gmail.com,25,,9876543214
```

The dataset intentionally contains data-quality issues such as missing values, extra spaces, invalid numeric values, and duplicate records to demonstrate the cleaning capabilities of the pipeline.

---

# Generic Design
Although the sample dataset is customer data, the pipeline does **not** contain customer-specific processing rules.
For example, the cleaning module does not assume that the dataset must contain:
```text
customer_id
name
email
age
city
phone
```
Instead, it automatically examines the available columns and applies generic processing rules.
Therefore, the same pipeline can be used for datasets such as:
```text
Customers
Employees
Students
Products
Orders
Sales
Movies
Books
Weather
```
without rewriting the core cleaning logic.
---
# Configuration
Pipeline settings are stored in:
```text
config/config.json
```
Example:
```json
{
    "input_file": "data/input/customers.csv",
    "input_type": "csv",
    "output_file": "data/output/cleaned_data.csv",
    "log_file": "logs/pipeline.log"
}
```
The configuration allows input and output paths to be changed without modifying the Python source code.
---
# Installation
## 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```
Navigate into the project:
```bash
cd data-processing-pipeline
```

---

## 2. Create a virtual environment
```bash
python -m venv venv
```
### Windows
```bash
venv\Scripts\activate
```
## 3. Install dependencies
```bash
pip install -r requirements.txt
```

If the requirements file has not been generated yet:

```bash
pip install pandas requests pytest
```

Then generate it using:

```bash
pip freeze > requirements.txt
```

---

# Running the Pipeline

Place the input file inside:

```text
data/input/
```

For the current example:

```text
data/input/customers.csv
```

Make sure `config/config.json` contains:

```json
{
    "input_file": "data/input/customers.csv",
    "input_type": "csv",
    "output_file": "data/output/cleaned_data.csv",
    "log_file": "logs/pipeline.log"
}
```

Run the pipeline from the project root:

```bash
python src/main.py
```

Example terminal output:

```text
Pipeline completed successfully!
-------------------------------
Input rows       : 10
Output rows      : 9
Output columns   : 6
Output file      : data/output/cleaned_data.csv
-------------------------------
```

The processed file will be available at:

```text
data/output/cleaned_data.csv
```

---

# Data Quality Report

The pipeline generates basic information about the dataset, including:

```text
Rows
Columns
Duplicate records
Missing values
```

This helps identify the overall quality of the input and processed data.

Example:

```text
Input Quality Report
--------------------
Rows              : 10
Columns           : 6
Duplicate Rows    : 1
Missing Values    : 3
```

---

# Logging

Pipeline execution details are stored in:

```text
logs/pipeline.log
```

Example:

```text
INFO - Pipeline started
INFO - Loading input data
INFO - Loaded 10 rows and 6 columns
INFO - Validation successful
INFO - Cleaning data
INFO - Transformation completed
INFO - Output saved to data/output/cleaned_data.csv
INFO - Pipeline completed successfully
```

Errors are also recorded in the log file to help with debugging.

---

# Error Handling

The pipeline handles common processing problems such as:

* Missing input files
* Empty datasets
* Unsupported input types
* Invalid API responses
* Invalid values
* File reading errors
* Unexpected processing errors

Errors are displayed in the terminal and recorded in the log.

---

# Testing

Automated tests are included using Pytest.

Run:

```bash
pytest
```

Example:

```text
2 passed
```

The tests verify important processing behavior such as missing-value handling and data transformations.

---

# Output

The cleaned dataset is saved to:

```text
data/output/cleaned_data.csv
```

The output contains standardized and cleaned data that can be used for further analysis or downstream processing.

---

# Design Principles

## Generic

The pipeline does not depend on a particular dataset or business domain.

## Modular

Data ingestion, cleaning, validation, transformation, configuration, and logging are implemented in separate modules.

## Configurable

Input and output locations can be changed through `config.json`.

## Reusable

The same pipeline can process different datasets without modifying the core cleaning code.

## Maintainable

The modular architecture makes it easier to add new data sources and processing operations.

---

# Future Improvements

The pipeline can be extended with:

* Automatic CSV/JSON file-type detection
* Excel file support
* Database connectivity
* Advanced data profiling
* Outlier detection
* Configurable missing-value strategies
* Rejected-record output
* JSON output
* Command-line arguments
* API retry mechanism
* Parallel processing for large datasets
* Docker support
* GitHub Actions CI/CD
* Data visualization dashboard

---

# Learning Outcomes

This project demonstrates practical experience with:

* Python
* Pandas
* Data ingestion
* ETL pipeline design
* Data cleaning
* Data validation
* Missing-value handling
* Data type conversion
* REST API integration
* Logging
* Configuration management
* Exception handling
* Automated testing
* Git and GitHub

---

# Author

**Shaikh Ayesha Lukman**

Data Processing Pipeline – Internship Project
