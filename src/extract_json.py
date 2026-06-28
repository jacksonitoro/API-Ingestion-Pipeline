import json
from datetime import datetime

import requests

from config import OPEN_BREWERY_API_URL, RAW_JSON_DIR
from logger import get_logger


def extract_breweries_json():
    logger = get_logger("extract_json")

    RAW_JSON_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = RAW_JSON_DIR / f"openbrewery_raw_{timestamp}.json"

    try:
        logger.info("Requesting data from %s", OPEN_BREWERY_API_URL)

        response = requests.get(OPEN_BREWERY_API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

        logger.info("Saved raw JSON file: %s", output_file)
        logger.info("HTTP status code: %s", response.status_code)
        logger.info("Response size (characters): %s", len(response.text))
        logger.info("Number of records fetched: %s", len(data))

        return output_file

    except requests.exceptions.Timeout:
        logger.error("Request timed out while calling the API.")
    except requests.exceptions.HTTPError as e:
        logger.error("HTTP error occurred: %s", e)
    except requests.exceptions.RequestException as e:
        logger.error("Request failed: %s", e)
    except json.JSONDecodeError as e:
        logger.error("Failed to decode JSON response: %s", e)
    except Exception as e:
        logger.error("Unexpected error: %s", e)

    return None