import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "database.db"

SCHEMA_PATH = BASE_DIR / "schema.sql"

def get_connection():
    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    return connection

def initialize_database():

    connection = get_connection()

    cursor = connection.cursor()

    with open(SCHEMA_PATH, "r", encoding="utf-8") as file:

        schema_sql = file.read()

    cursor.executescript(schema_sql)

    connection.commit()
    connection.close()