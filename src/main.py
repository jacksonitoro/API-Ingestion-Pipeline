from logger import get_logger
from config import (
    RAW_JSON_DIR,
    RAW_CSV_DIR,
    PROCESSED_DIR,
    LOGS_DIR,
    SQL_DIR,
    OPEN_BREWERY_API_URL,
    SAMPLE_CSV_URL,
    SQLITE_DB_PATH,
)
from extract_json import extract_breweries_json


def ensure_directories():
    for path in [RAW_JSON_DIR, RAW_CSV_DIR, PROCESSED_DIR, LOGS_DIR, SQL_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def main():
    ensure_directories()

    logger = get_logger("main")
    logger.info("Pipeline project started successfully.")
    logger.info("JSON API source: %s", OPEN_BREWERY_API_URL)
    logger.info("CSV source: %s", SAMPLE_CSV_URL)
    logger.info("Raw JSON directory: %s", RAW_JSON_DIR)
    logger.info("Raw CSV directory: %s", RAW_CSV_DIR)
    logger.info("Processed directory: %s", PROCESSED_DIR)
    logger.info("SQLite DB path: %s", SQLITE_DB_PATH)

    json_file = extract_breweries_json()

    if json_file:
        logger.info("JSON extraction completed successfully: %s", json_file)
    else:
        logger.warning("JSON extraction did not complete successfully.")


if __name__ == "__main__":
    main()