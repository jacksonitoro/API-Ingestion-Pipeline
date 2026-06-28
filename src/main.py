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
from extract_csv import extract_sample_csv
from transform_json import transform_breweries_json
from transform_csv import transform_sample_csv
from load_sqlite import load_to_sqlite
from validate_load import validate_load


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

    csv_file = extract_sample_csv()
    if csv_file:
        logger.info("CSV extraction completed successfully: %s", csv_file)
    else:
        logger.warning("CSV extraction did not complete successfully.")

    processed_json_file = transform_breweries_json()
    if processed_json_file:
        logger.info("JSON transformation completed successfully: %s", processed_json_file)
    else:
        logger.warning("JSON transformation did not complete successfully.")

    processed_csv_file = transform_sample_csv()
    if processed_csv_file:
        logger.info("CSV transformation completed successfully: %s", processed_csv_file)
    else:
        logger.warning("CSV transformation did not complete successfully.")

    try:
        load_to_sqlite()
        load_ok = True
        logger.info("SQLite load completed.")
    except Exception as e:
        load_ok = False
        logger.error("SQLite load failed: %s", e)

    validation_ok = validate_load()
    if validation_ok:
        logger.info("Load validation completed successfully.")
    else:
        logger.warning("Load validation found issues.")

    all_ok = all([
        json_file is not None,
        csv_file is not None,
        processed_json_file is not None,
        processed_csv_file is not None,
        load_ok,
        validation_ok,
    ])

    if all_ok:
        logger.info("Pipeline run completed successfully.")
    else:
        logger.warning("Pipeline run completed with issues.")


if __name__ == "__main__":
    main()