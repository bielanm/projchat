from functools import lru_cache
import os
import psycopg2


@lru_cache(1)
def get_connection():
    db_name = os.getenv("DB_NAME", "example")
    user_name = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "password")
    host = os.getenv("DB_HOST", "localhost")
    return psycopg2.connect(host=host, user=user_name, password=password, database=db_name)