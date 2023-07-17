from psycopg2 import OperationalError
from .connector import conn


def execute_query(query, connection=conn):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Executed!")
    except OperationalError as err:
        print(f"Error <{err}> occurred.")


create_msg_table = """
CREATE TABLE IF NOT EXISTS messages (
    id SERIAL PRIMARY KEY,
    message TEXT,
    user_id BIGINT NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
);
"""

fill_msg_table = """
INSERT INTO public.messages (message, user_id, message_time)
SELECT
    md5(random()::text) AS message,
    floor(random() * 1000000)::int AS user_id,
    '2023-07-13 10:30:00+00:00'::timestamp + (random() * interval '1 day') AS message_time
FROM generate_series(1, 100);
"""

execute_query(create_msg_table)
# execute_query(fill_msg_table)
