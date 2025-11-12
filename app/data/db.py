import sqlite3
from pathlib import Path

DB_PATH = Path("/home/farhad/Documents/CW2_CST1510_M01039453/DATA/intelligence_platform.db")    

def connect_database(db_path=DB_PATH):
    """Connect to the SQLite database."""
    conn = sqlite3.connect(db_path)
    return conn

# Test the connection
test_conn = connect_database()
print(" Database connection successful!")
print(f"Database type: {type(test_conn)}")
test_conn.close()
print(" Connection closed.")