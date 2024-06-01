import zipfile
import os
import sqlite3
import pandas as pd

"""
    Converting anki files to txt format.
"""


def extract_apkg(input_path, export_path):
    """
    Extracts the contents of an Anki .apkg file to a specified directory.

    :param input_path: Path to the .apkg file.
    :param export_path: Directory where the contents will be extracted.
    """
    with zipfile.ZipFile(input_path, 'r') as zip_ref:
        zip_ref.extractall(export_path)


def connect_to_db(database_path):
    """
    Connects to the SQLite database at the given path.

    :param database_path: Path to the SQLite database file.
    :return: SQLite connection object.
    """
    connection = sqlite3.connect(database_path)
    return connection


def fetch_tables(connection):
    """
    Fetches the names of all tables in the SQLite database.

    :param connection: SQLite connection object.
    :return: List of table names.
    """
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables


def fetch_table_data(connection, table_name):
    """
    Fetches all data from a specified table in the SQLite database.

    :param connection: SQLite connection object.
    :param table_name: Name of the table to fetch data from.
    :return: DataFrame containing the table data.
    """
    query = f"SELECT * FROM {table_name}"
    data_frame = pd.read_sql_query(query, connection)
    return data_frame


def main(apkg_file_path, extraction_directory):
    """
    Main function to extract Anki .apkg file, connect to the SQLite database,
    and print the table names and data from the 'notes' table.

    :param apkg_file_path: Path to the .apkg file.
    :param extraction_directory: Directory where the contents will be extracted.
    """
    extract_apkg(apkg_file_path, extraction_directory)

    db_file_path = os.path.join(extraction_directory, 'collection.anki2')
    db_connection = connect_to_db(db_file_path)

    table_names = fetch_tables(db_connection)
    print("Tables in the database:", table_names)

    # Example: Fetch data from the 'notes' table
    notes_table = 'notes'
    notes_data = fetch_table_data(db_connection, notes_table)
    print(notes_data.head())


if __name__ == '__main__':
    apkg_path = 'collection.anki2.apkg'
    extract_to = '.'  # Extract to current directory
    extract_apkg(apkg_path, extract_to)
