import sqlite3
import pandas as pd
from pathlib import Path
from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import register_user, login_user, migrate_users_from_file
from app.data.incidents import insert_incident, get_all_incidents

DATA_DIR = Path("CW2_CST1510_M01039453/DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

def load_csv_to_table(conn, csv_path, table_name):
    """Load a CSV file into a database table using pandas."""
    path = Path(csv_path)
    
    # Check if file exists
    if not path.exists():
        print(f" Warning: {csv_path} not found. Skipping.")
        return 0
    
    # Read CSV into DataFrame
    df = pd.read_csv(path)
    
    # Clean column names (remove extra whitespace)
    df.columns = df.columns.str.strip()
    
    # Preview data
    print(f"\n Loading {csv_path}...")
    print(f"   Columns: {list(df.columns)}")
    print(f"   Rows: {len(df)}")
    
    # Load into database
    df.to_sql(table_name, conn, if_exists='append', index=False)
    
    print(f"    Loaded {len(df)} rows into '{table_name}' table.")
    return len(df)

def load_all_csv_data(conn):
    """
    Load all three domain CSV files into the database.
    """
    print("\n Starting CSV data loading...")
    
    total_rows = 0
    
    # Load cyber incidents
    total_rows += load_csv_to_table(
        conn,
        DATA_DIR / "cyber_incidents.csv",
        "cyber_incidents"
    )
    
    # Load datasets metadata
    total_rows += load_csv_to_table(
        conn,
        DATA_DIR / "datasets_metadata.csv",
        "datasets_metadata"
    )
    
    # Load IT tickets
    total_rows += load_csv_to_table(
        conn,
        DATA_DIR / "it_tickets.csv",
        "it_tickets"
    )
    
    print(f"\nTotal rows loaded: {total_rows}")
    return total_rows

def setup_database_complete():
    """
    Complete database setup:
    1. Connect to database
    2. Create all tables
    3. Migrate users from users.txt
    4. Load CSV data for all domains
    5. Verify setup
    """
    print("\n" + "="*60)
    print("STARTING COMPLETE DATABASE SETUP")
    print("="*60)
    
    # Step 1: Connect
    print("\n[1/5] Connecting to database...")
    conn = connect_database()
    print("       Connected")
    
    # Step 2: Create tables
    print("\n[2/5] Creating database tables...")
    create_all_tables(conn)
    
    # Step 3: Migrate users
    print("\n[3/5] Migrating users from users.txt...")
    user_count = migrate_users_from_file(conn)
    print(f"       Migrated {user_count} users")
    
    # Step 4: Load CSV data
    print("\n[4/5] Loading CSV data...")
    total_rows = load_all_csv_data(conn)
    
    # Step 5: Verify
    print("\n[5/5] Verifying database setup...")
    cursor = conn.cursor()
    
    # Count rows in each table
    tables = ['users', 'cyber_incidents', 'datasets_metadata', 'it_tickets']
    print("\n Database Summary:")
    print(f"{'Table':<25} {'Row Count':<15}")
    print("-" * 40)
    
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"{table:<25} {count:<15}")
    
    conn.close()
    
    print("\n" + "="*60)
    print(" DATABASE SETUP COMPLETE!")
    print("="*60)
    print(f"\n Database location: {DB_PATH.resolve()}")
    print("\nYou're ready for Week 9 (Streamlit web interface)!")


