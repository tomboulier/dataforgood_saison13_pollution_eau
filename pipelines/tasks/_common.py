import os
import glob


ROOT_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
DATABASE_FOLDER = os.path.join(ROOT_FOLDER, "database")
DUCKDB_FILE = os.path.join(DATABASE_FOLDER, "data.duckdb")
CACHE_FOLDER = os.path.join(ROOT_FOLDER, "database", "cache")

os.makedirs(CACHE_FOLDER, exist_ok=True)
os.makedirs(DATABASE_FOLDER, exist_ok=True)


def clear_cache():
    """Clear the cache folder."""
    for file in glob.glob(os.path.join(CACHE_FOLDER, "*")):
        os.remove(file)
