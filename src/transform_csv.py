import pandas as pd

from config import RAW_CSV_DIR, PROCESSED_DIR
from logger import get_logger


def get_latest_csv_file():
    csv_files = list(RAW_CSV_DIR.glob("airtravel_raw_*.csv"))
    return max(csv_files, key=lambda f: f.stat().st_mtime) if csv_files else None


def transform_sample_csv():
    logger = get_logger("transform_csv")

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    latest_file = get_latest_csv_file()

    if not latest_file:
        logger.warning("No raw CSV files found for transformation.")
        return None

    try:
        logger.info("Reading raw CSV file: %s", latest_file)

        df = pd.read_csv(latest_file)

        df.columns = [
            col.strip().replace('"', "").lower().replace(" ", "_")
            for col in df.columns
        ]

        output_file = PROCESSED_DIR / "airtravel_processed.csv"
        df.to_csv(output_file, index=False)

        logger.info("Processed CSV saved to: %s", output_file)
        logger.info("Number of rows written: %s", len(df))
        logger.info("Number of columns written: %s", len(df.columns))
        logger.info("Processed CSV columns: %s", list(df.columns))

        return output_file

    except Exception as e:
        logger.error("Failed to transform CSV file: %s", e)
        return None