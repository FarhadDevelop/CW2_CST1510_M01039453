import sqlite3
from pathlib import Path

DATA_DIR = Path("CW2_CST1510_M01039453/my_app/DATA copy")
DB_PATH = DATA_DIR / "intelligence_platform.db"  

def connect_database(db_path=DB_PATH):
    """
    Connect to the SQLite database.
    
    Args:
        db_path (Path): The path to the SQLite database file.

    Returns:
        sqlite3.Connection: The database connection object.
    """
    conn = sqlite3.connect(str(db_path))
    return conn
