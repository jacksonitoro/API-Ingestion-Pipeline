import sqlite3
from pathlib import Path

import pandas as pd

from config import PROCESSED_DIR, SQLITE_DB_PATH
from logger import get_logger


def load_processed_csv(csv_path, table_name, logger):
    df = pd.read_csv(csv_path)

    with sqlite3.connect(SQLITE_DB_PATH) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    logger.info("Loaded %s rows into table %s", len(df), table_name)


def load_to_sqlite():
    logger = get_logger("load_sqlite")

    brewery_file = PROCESSED_DIR / "breweries_processed.csv"
    airtravel_file = PROCESSED_DIR / "airtravel_processed.csv"

    if not brewery_file.exists():
        logger.warning("Breweries processed file not found: %s", brewery_file)
    else:
        load_processed_csv(brewery_file, "breweries", logger)

    if not airtravel_file.exists():
        logger.warning("Airtravel processed file not found: %s", airtravel_file)
    else:
        load_processed_csv(airtravel_file, "airtravel", logger)


if __name__ == "__main__":
    load_to_sqlite()