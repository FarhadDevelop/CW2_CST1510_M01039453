import sqlite3
from pathlib import Path

# Define the path to the database
DATA_DIR = Path("CW2_CST1510_M01039453/DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

# Import the connect_database function from db.py
from db import connect_database

def create_users_table(conn):
    """Create the users table."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT DEFAULT 'user'
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("Users table created successfully.")

def create_cyber_incidents_table(conn):
    """Create the cyber_incidents table."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS cyber_incidents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        severity TEXT NOT NULL,
        status TEXT DEFAULT 'open',
        date TEXT
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("Cyber incidents table created successfully.")

def create_datasets_metadata_table(conn):
    """Create the datasets_metadata table."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS datasets_metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        source TEXT,
        category TEXT,
        size INTEGER
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("Datasets metadata table created successfully.")

def create_it_tickets_table(conn):
    """Create the it_tickets table."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS it_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        priority TEXT NOT NULL,
        status TEXT DEFAULT 'open',
        created_date TEXT
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("IT tickets table created successfully.")

def create_all_tables(conn):
    """Create all tables in the database."""
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)
    print("\nAll tables created successfully.")





    





