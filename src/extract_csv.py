from datetime import datetime

import requests

from config import SAMPLE_CSV_URL, RAW_CSV_DIR
from logger import get_logger


def extract_sample_csv():
    logger = get_logger("extract_csv")

    RAW_CSV_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = RAW_CSV_DIR / f"airtravel_raw_{timestamp}.csv"

    try:
        logger.info("Requesting CSV from %s", SAMPLE_CSV_URL)

        response = requests.get(SAMPLE_CSV_URL, timeout=10)
        response.raise_for_status()

        with open(output_file, "wb") as file:
            file.write(response.content)

        logger.info("Saved raw CSV file: %s", output_file)
        logger.info("HTTP status code: %s", response.status_code)
        logger.info("Response size (bytes): %s", len(response.content))

        return output_file

    except requests.exceptions.Timeout:
        logger.error("Request timed out while downloading the CSV.")
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP error occurred: %s", e)
    except requests.exceptions.RequestException as e:
        logger.error("Request failed: %s", e)
    except Exception as e:
        logger.error("Unexpected error: %s", e)

    return None