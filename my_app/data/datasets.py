import sqlite3
import pandas as pd
from app.data.db import connect_database

def create_dataset_metadata(conn, name, rows, columns, uploaded_by, upload_date):
    """
    Insert a new dataset metadata record into the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        name (str): The name of the dataset.
        rows (int): The number of rows in the dataset.
        columns (int): The number of columns in the dataset.
        uploaded_by (str): The user who uploaded the dataset.
        upload_date (str): The date the dataset was uploaded.
    
    Returns:
        int: The ID of the newly created dataset metadata record.
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets_metadata (name, rows, columns, uploaded_by, upload_date)
        VALUES (?, ?, ?, ?, ?)
    """, (name, rows, columns, uploaded_by, upload_date))
    conn.commit()
    return cursor.lastrowid

def get_all_datasets_metadata(conn):
    """
    Retrieve all dataset metadata records from the database.

    Args:
        conn (sqlite3.Connection): The database connection.

    Returns:
        pd.DataFrame: A DataFrame containing all dataset metadata records.
    """
    query = "SELECT * FROM datasets_metadata"
    df = pd.read_sql_query(query, conn)
    return df

def update_dataset_uploaded_by(conn, dataset_id, new_uploaded_by):
    """
    Update the uploaded_by field of a dataset metadata record.

    Args:
        conn (sqlite3.Connection): The database connection.
        dataset_id (int): The ID of the dataset metadata record to update.
        new_uploaded_by (str): The new uploaded_by value.
    
    Returns:
        int: The number of rows affected.
    """
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE datasets_metadata
        SET uploaded_by = ?
        WHERE dataset_id = ?
    """, (new_uploaded_by, dataset_id))
    conn.commit()
    return cursor.rowcount

def delete_dataset_metadata(conn, dataset_id):
    """
    Delete a dataset metadata record from the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        dataset_id (int): The ID of the dataset metadata record to delete.
    
    Returns:
        int: The number of rows affected.
    """
    cursor = conn.cursor()
    cursor.execute("DELETE FROM datasets_metadata WHERE dataset_id = ?", (dataset_id,))
    conn.commit()
    return cursor.rowcount

