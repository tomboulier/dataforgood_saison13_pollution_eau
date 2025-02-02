import os

from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the .env file
dotenv_path = os.path.join(current_dir, ".env")


def load_env_variables():
    load_dotenv(dotenv_path)
