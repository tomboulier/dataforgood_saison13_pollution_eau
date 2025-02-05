from typing import Dict


def get_edc_config() -> Dict:
    """
    Returns various configuration for processing the EDC (Eau distribuée par commune) datasets.
    The data comes from https://www.data.gouv.fr/fr/datasets/resultats-du-controle-sanitaire-de-leau-distribuee-commune-par-commune/
    For each year a dataset is downloadable on a URL like this (ex. 2024):
        https://www.data.gouv.fr/fr/datasets/r/84a67a3b-08a7-4001-98e6-231c74a98139
    :return: A dict with the config used for processing.
        The "source" part is related to the data.gouv datasource
        The "files" part is related to the extracted files information and sql table names
    """

    edc_config = {
        "source": {
            "base_url": "https://www.data.gouv.fr/fr/datasets/r/",
            "available_years": [
                "2016",
                "2017",
                "2018",
                "2019",
                "2020",
                "2021",
                "2022",
                "2023",
                "2024",
            ],
            "yearly_files_infos": {
                "2024": {
                    "id": "84a67a3b-08a7-4001-98e6-231c74a98139",
                    "zipfile": "dis-2024.zip",
                },
                "2023": {
                    "id": "c89dec4a-d985-447c-a102-75ba814c398e",
                    "zipfile": "dis-2023.zip",
                },
                "2022": {
                    "id": "a97b6074-c4dd-4ef2-8922-b0cf04dbff9a",
                    "zipfile": "dis-2022.zip",
                },
                "2021": {
                    "id": "d2b432cc-3761-44d3-8e66-48bc15300bb5",
                    "zipfile": "dis-2021.zip",
                },
                "2020": {
                    "id": "a6cb4fea-ef8c-47a5-acb3-14e49ccad801",
                    "zipfile": "dis-2020.zip",
                },
                "2019": {
                    "id": "861f2a7d-024c-4bf0-968b-9e3069d9de07",
                    "zipfile": "dis-2019.zip",
                },
                "2018": {
                    "id": "0513b3c0-dc18-468d-a969-b3508f079792",
                    "zipfile": "dis-2018.zip",
                },
                "2017": {
                    "id": "5785427b-3167-49fa-a581-aef835f0fb04",
                    "zipfile": "dis-2017.zip",
                },
                "2016": {
                    "id": "483c84dd-7912-483b-b96f-4fa5e1d8651f",
                    "zipfile": "dis-2016.zip",
                },
            },
        },
        "files": {
            "communes": {
                "file_name_prefix": "DIS_COM_UDI_",
                "file_extension": ".txt",
                "table_name": "edc_communes",
            },
            "prelevements": {
                "file_name_prefix": "DIS_PLV_",
                "file_extension": ".txt",
                "table_name": "edc_prelevements",
            },
            "resultats": {
                "file_name_prefix": "DIS_RESULT_",
                "file_extension": ".txt",
                "table_name": "edc_resultats",
            },
        },
    }

    return edc_config


def create_edc_yearly_filename(
    file_name_prefix: str, file_extension: str, year: str
) -> str:
    """
    This function is used to recreate the yearly filenames of the extracted files.
    It is intended for use with the edc_config["files"] data above.
    For example in 2024 the file name for communes should be:
        DIS_COM_UDI_2024.txt
    :param file_name_prefix: prefix of the filename
    :param file_extension: extension of the file
    :param year: year of the needed file
    :return: the yearly filename as a string
    """
    return file_name_prefix + year + file_extension
