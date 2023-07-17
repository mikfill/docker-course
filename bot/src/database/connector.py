from psycopg2 import OperationalError, connect
from bot.src.settings import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT


def create_connection(
    db_name=DB_NAME,
    db_user=DB_USER,
    db_password=DB_PASSWORD,
    db_host=DB_HOST,
    db_port=DB_PORT,
):
    try:
        print("Connecting...")
        connection = connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection successful!")
    except OperationalError as err:
        print(f"The error <{err}> occured")
        connection = None
    return connection


conn = create_connection()
