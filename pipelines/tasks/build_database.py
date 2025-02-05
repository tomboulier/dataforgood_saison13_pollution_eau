"""
Consolidate data into the database.
"""

import logging
import os
from typing import List, Literal
from zipfile import ZipFile

import duckdb
import requests

from ._common import CACHE_FOLDER, DUCKDB_FILE, clear_cache
from ._config_edc import get_edc_config, create_edc_yearly_filename

logger = logging.getLogger(__name__)
edc_config = get_edc_config()


def check_table_existence(conn: duckdb.DuckDBPyConnection, table_name: str) -> bool:
    """
    Check if a table exists in the duckdb database
    :param conn: The duckdb connection to use
    :param table_name: The table name to check existence
    :return: True if the table exists, False if not
    """
    query = f"""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{table_name}'
        """
    conn.execute(query)
    return list(conn.fetchone())[0] == 1


def download_extract_insert_yearly_edc_data(year: str):
    """
    Downloads from www.data.gouv.fr the EDC (Eau distribuée par commune) dataset for one year,
    extracts the files and insert the data into duckdb
    :param year: The year from which we want to download the dataset
    :return: Create or replace the associated tables in the duckcb database.
        It adds the column "de_partition" based on year as an integer.
    """

    # Dataset specific constants
    DATA_URL = (
        edc_config["source"]["base_url"]
        + edc_config["source"]["yearly_files_infos"][year]["id"]
    )
    ZIP_FILE = os.path.join(
        CACHE_FOLDER, edc_config["source"]["yearly_files_infos"][year]["zipfile"]
    )
    EXTRACT_FOLDER = os.path.join(CACHE_FOLDER, f"raw_data_{year}")
    FILES = edc_config["files"]

    logger.info(f"Processing EDC dataset for {year}...")
    response = requests.get(DATA_URL, stream=True)
    with open(ZIP_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    logger.info("   Extracting files...")
    with ZipFile(ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(EXTRACT_FOLDER)

    logger.info("   Creating or updating tables in the database...")
    conn = duckdb.connect(DUCKDB_FILE)

    for file_info in FILES.values():
        filepath = os.path.join(
            EXTRACT_FOLDER,
            create_edc_yearly_filename(
                file_name_prefix=file_info["file_name_prefix"],
                file_extension=file_info["file_extension"],
                year=year,
            ),
        )

        if check_table_existence(conn=conn, table_name=f"{file_info['table_name']}"):
            query = f"""
                DELETE FROM {f"{file_info['table_name']}"}
                WHERE de_partition = CAST({year} as INTEGER)
                ;
            """
            conn.execute(query)
            query_start = f"INSERT INTO {f'{file_info["table_name"]}'} "

        else:
            query_start = f"CREATE TABLE {f'{file_info["table_name"]}'} AS "

        query_select = f"""
            SELECT 
                *,
                CAST({year} AS INTEGER) AS de_partition,
                current_date            AS de_ingestion_date
            FROM read_csv('{filepath}', header=true, delim=',');
        """

        conn.execute(query_start + query_select)

    conn.close()

    logger.info("   Cleaning up cache...")
    clear_cache()

    return True


def process_edc_datasets(
    refresh_type: Literal["all", "last", "custom"] = "last",
    custom_years: List[str] = None,
):
    """
    Process the EDC datasets.
    :param refresh_type: Refresh type to run
        - "all": Refresh the data for every possible year
        - "last": Refresh the data only for the last available year
        - "custom": Refresh the data for the years specified in the list custom_years
    :param custom_years: years to update
    :return:
    """
    available_years = edc_config["source"]["available_years"]

    if refresh_type == "all":
        years_to_update = available_years
    elif refresh_type == "last":
        years_to_update = available_years[-1:]
    elif refresh_type == "custom":
        if custom_years:
            years_to_update = list(set(custom_years).intersection(available_years))
        else:
            raise ValueError(
                """ custom_years parameter needs to be specified if refresh_type="custom" """
            )
    else:
        raise ValueError(
            f""" refresh_type needs to be one of ["all", "last", "custom"], it can't be: {refresh_type}"""
        )

    logger.info(f"Launching processing of EDC datasets for years: {years_to_update}")

    for year in years_to_update:
        download_extract_insert_yearly_edc_data(year=year)

    logger.info("Cleaning up cache...")
    clear_cache(recreate_folder=False)
    return True


def execute():
    process_edc_datasets()
