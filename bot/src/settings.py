import logging
import os

from dotenv import load_dotenv

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
load_dotenv()

try:
    DB_NAME = os.environ["PG_NAME"]
    DB_USER = os.environ["PG_USER"]
    DB_PASSWORD = os.environ["PG_PASSWORD"]
    DB_HOST = os.environ["PG_HOST"]
    DB_PORT = os.environ["PG_PORT"]
except KeyError as err:
    logging.critical(f"Can`t read tocken from enviroment variable. Message: {err}")
    raise KeyError(err)

try:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
except KeyError as err:
    logging.critical(f"Can`t read tocken from enviroment variable. Message: {err}")
    raise KeyError(err)
