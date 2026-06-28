import json
from pathlib import Path

import pandas as pd

from config import RAW_JSON_DIR, PROCESSED_DIR
from logger import get_logger


def get_latest_json_file():
    json_files = sorted(RAW_JSON_DIR.glob("openbrewery_raw_*.json"))
    return json_files[-1] if json_files else None


def transform_breweries_json():
    logger = get_logger("transform_json")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    latest_file = get_latest_json_file()

    if not latest_file:
        logger.warning("No raw JSON files found for transformation.")
        return None

    try:
        logger.info("Reading raw JSON file: %s", latest_file)

        with open(latest_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        df = pd.json_normalize(data)

        output_file = PROCESSED_DIR / "breweries_processed.csv"
        df.to_csv(output_file, index=False)

        logger.info("Processed JSON saved to: %s", output_file)
        logger.info("Number of rows written: %s", len(df))
        logger.info("Number of columns written: %s", len(df.columns))

        return output_file

    except Exception as e:
        logger.error("Failed to transform JSON file: %s", e)
        return None