import sqlite3
from app.data.db import connect_database

def create_dataset_metadata(conn, name, rows, columns, uploaded_by, upload_date):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO datasets_metadata (name, rows, columns, uploaded_by, upload_date)
        VALUES (?, ?, ?, ?, ?)
    """, (name, rows, columns, uploaded_by, upload_date))
    conn.commit()
    return cursor.lastrowid

def get_all_datasets_metadata(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM datasets_metadata")
    return cursor.fetchall()

def update_dataset_uploaded_by(conn, dataset_id, new_uploaded_by):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE datasets_metadata
        SET uploaded_by = ?
        WHERE id = ?
    """, (new_uploaded_by, dataset_id))
    conn.commit()
    return cursor.rowcount

def delete_dataset_metadata(conn, dataset_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM datasets_metadata WHERE id = ?", (dataset_id,))
    conn.commit()
    return cursor.rowcount

