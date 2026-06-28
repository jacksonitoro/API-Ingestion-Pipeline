from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_JSON_DIR = RAW_DIR / "json"
RAW_CSV_DIR = RAW_DIR / "csv"
PROCESSED_DIR = DATA_DIR / "processed"
LOGS_DIR = BASE_DIR / "logs"
SQL_DIR = BASE_DIR / "sql"

OPEN_BREWERY_API_URL = "https://api.openbrewerydb.org/v1/breweries"
SAMPLE_CSV_URL = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv"

SQLITE_DB_PATH = BASE_DIR / "brewery_pipeline.db"