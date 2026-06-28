import sqlite3

from config import SQLITE_DB_PATH
from logger import get_logger


def table_exists(conn, table_name):
    cur = conn.cursor()
    cur.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,),
    )
    return cur.fetchone() is not None


def get_row_count(conn, table_name):
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    return cur.fetchone()[0]


def validate_load():
    logger = get_logger("validate_load")

    expected_counts = {
        "breweries": 50,
        "airtravel": 12,
    }

    try:
        with sqlite3.connect(SQLITE_DB_PATH) as conn:
            all_passed = True

            for table_name, expected_count in expected_counts.items():
                if not table_exists(conn, table_name):
                    logger.error("Table missing: %s", table_name)
                    all_passed = False
                    continue

                actual_count = get_row_count(conn, table_name)

                if actual_count == expected_count:
                    logger.info(
                        "PASS | %s | expected=%s actual=%s",
                        table_name,
                        expected_count,
                        actual_count,
                    )
                else:
                    logger.error(
                        "FAIL | %s | expected=%s actual=%s",
                        table_name,
                        expected_count,
                        actual_count,
                    )
                    all_passed = False

            return all_passed

    except Exception as e:
        logger.error("Validation failed: %s", e)
        return False