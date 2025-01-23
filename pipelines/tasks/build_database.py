"""
Consolidate data into the database.
"""

import logging
import os
from zipfile import ZipFile

import duckdb
import requests

from ._common import CACHE_FOLDER, DUCKDB_FILE, clear_cache

logger = logging.getLogger(__name__)


def process_sise_eaux_dataset_2024():
    """Process SISE-Eaux dataset for 2024."""

    # Dataset specific constants
    DATA_URL = (
        "https://www.data.gouv.fr/fr/datasets/r/84a67a3b-08a7-4001-98e6-231c74a98139"
    )
    ZIP_FILE = os.path.join(CACHE_FOLDER, "dis-2024.zip")
    EXTRACT_FOLDER = os.path.join(CACHE_FOLDER, "raw_data_2024")

    FILES = {
        "communes": {"filename": "DIS_COM_UDI_2024.txt", "table": "sise_communes"},
        "prelevements": {"filename": "DIS_PLV_2024.txt", "table": "sise_prelevements"},
        "resultats": {"filename": "DIS_RESULT_2024.txt", "table": "sise_resultats"},
    }

    logger.info("Downloading and extracting SISE-Eaux dataset for 2024...")
    response = requests.get(DATA_URL, stream=True)
    with open(ZIP_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    logger.info("Extracting files...")
    with ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)

    logger.info("Creating tables in the database...")
    conn = duckdb.connect(DUCKDB_FILE)
    for file_info in FILES.values():
        filepath = os.path.join(EXTRACT_FOLDER, file_info["filename"])
        query = f"""
            CREATE OR REPLACE TABLE {file_info["table"]} AS 
            SELECT * FROM read_csv('{filepath}', header=true, delim=',');
        """
        conn.execute(query)
    conn.close()

    logger.info("Cleaning up...")
    clear_cache()

    return True


def execute():
    process_sise_eaux_dataset_2024()
