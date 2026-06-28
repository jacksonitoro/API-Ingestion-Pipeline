# Public API Ingestion Pipeline

A beginner-friendly data engineering project that extracts data from a public JSON API and a public CSV source, stores raw files locally, transforms them into processed datasets, loads them into SQLite, and validates the final row counts.

## Project overview

This project simulates a small local batch ingestion pipeline using Python. It follows a simple extract-transform-load workflow and adds logging, validation, and a final pipeline run summary to improve reliability and observability.

## Data sources

- JSON API: Open Brewery DB
- CSV file: Air Travel CSV dataset

## Pipeline workflow

1. Extract JSON data from the Open Brewery DB API.
2. Save raw JSON files locally with timestamped filenames.
3. Extract CSV data from a public CSV source.
4. Save raw CSV files locally with timestamped filenames.
5. Transform raw JSON into a processed CSV file.
6. Transform raw CSV into a cleaned processed CSV file.
7. Load both processed datasets into SQLite tables.
8. Validate table row counts after load.
9. Write progress and results to logs.

## Repository structure

```text
public-api-ingestion-pipeline/
├── data/
│   ├── raw/
│   │   ├── json/
│   │   └── csv/
│   └── processed/
├── logs/
├── sql/
├── src/
│   ├── config.py
│   ├── extract_json.py
│   ├── extract_csv.py
│   ├── transform_json.py
│   ├── transform_csv.py
│   ├── load_sqlite.py
│   ├── validate_load.py
│   ├── logger.py
│   └── main.py
├── tests/
├── requirements.in
├── requirements.txt
├── brewery_pipeline.db
└── README.md
```

## Features implemented

- Public API ingestion with Python `requests`
- Public CSV ingestion
- Raw data storage with timestamped filenames
- JSON transformation into tabular format
- CSV cleaning and transformation
- SQLite database loading
- Post-load validation checks
- Console and file logging
- Final pipeline success summary

## Setup instructions

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the pipeline

From the project root:

```bash
python src/main.py
```

## Expected outputs

After a successful run, the project will produce:

- Raw JSON files in `data/raw/json/`
- Raw CSV files in `data/raw/csv/`
- Processed CSV files in `data/processed/`
- SQLite database file: `brewery_pipeline.db`
- Log file output in `logs/`

## Validation

The pipeline validates that:

- the `breweries` table exists,
- the `airtravel` table exists,
- the loaded row counts match expected values.

## Current status

Completed:

- JSON extraction
- CSV extraction
- JSON transformation
- CSV transformation
- SQLite loading
- Load validation
- Final run summary logging

## Next improvements

- Replace `to_sql()` with explicit SQLite schema creation
- Add stronger null and schema validation
- Add unit tests for extraction, transformation, and validation
- Improve retry handling and failure reporting
- Parameterize sources and output settings through configuration

## Skills demonstrated

- Python scripting
- API data ingestion
- CSV parsing
- JSON transformation
- Local batch pipeline design
- SQLite loading
- Logging and validation
- Basic data engineering workflow design