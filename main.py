import pandas as pd
from pathlib import Path
from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import migrate_users_from_file, register_user, login_user
from app.data.users import insert_user, get_user_by_username, update_user_role, delete_user
from app.data.incidents import insert_incident, get_all_incidents, update_incident_status, delete_incident
from app.data.datasets import create_dataset_metadata, get_all_datasets_metadata, update_dataset_uploaded_by, delete_dataset_metadata
from app.data.tickets import insert_ticket, get_all_tickets, update_ticket_status, delete_ticket

# Define paths
DATA_DIR = Path("CW2_CST1510_M01039453/DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

def load_csv_to_table(conn, csv_path, table_name):
    """
    Load a CSV file into a specified database table.

    Args:
        conn (sqlite3.Connection): The database connection.
        csv_path (Path): The path to the CSV file.
        table_name (str): The name of the database table to load data into.
    
    Returns:
        int: The number of rows loaded.
    """
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
    Load all CSV data files into their respective database tables.

    Args:
        conn (sqlite3.Connection): The database connection.
    
    Returns:
        int: The total number of rows loaded across all tables.
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

def main():
    """Main function to demonstrate database operations."""
    print("=" * 60)
    print("Week 8: Database Demo")
    print("=" * 60)

    # Setup database
    conn = connect_database()
    create_all_tables(conn)

    # Migrate users from file
    migrate_users_from_file(conn)

    # Test authentication
    success, msg = register_user('nathan', '!like@pizza')
    print(f"\n{msg}")

    success, msg = login_user('nathan', '!like@pizza')
    print(f"\n{msg}")

    # Load all CSV data into the database
    load_all_csv_data(conn)
    print("\nCSV Data Loaded Successfully.")
    
    # Display all users
    print("\nAll Users:")
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    print(users_df)

    # Display all cyber incidents
    print("\nAll Cyber Incidents:")
    incidents_df = pd.read_sql_query("SELECT * FROM cyber_incidents", conn)
    print(incidents_df)

    # Display all datasets metadata
    print("\nAll Datasets Metadata:")
    datasets_df = pd.read_sql_query("SELECT * FROM datasets_metadata", conn)
    print(datasets_df)

    # Display all IT tickets
    print("\nAll IT Tickets:")
    tickets_df = pd.read_sql_query("SELECT * FROM it_tickets", conn)
    print(tickets_df)

    # Insert a new user
    insert_user('bob', 'hashed_password_123', 'analyst')
    print("\nInserted New User:")
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    print(users_df)

    # Display all users
    user_by_username = get_user_by_username('bob')
    print("\nUser Retrieved by Username:")
    print(user_by_username)

    # Update user role
    update_user_role('alice', 'admin')
    print("\nUpdated User Role:")
    updated_user = get_user_by_username('alice')
    print(updated_user)

    # Delete a user
    delete_user('bob')
    print("\nUsers after Deletion:")
    deleted_user = get_user_by_username('bob')
    print(deleted_user)

    # Insert a cyber incident
    insert_incident(conn, '2024-06-01 12:00:00.000000', 'Phishing', 'High', 'Open', 'Phishing email reported by user')
    print("\nInserted Cyber Incident:")
    inserted_incident = get_all_incidents(conn)
    print(inserted_incident)

    # Retrieve and display all incidents
    get_all_incidents(conn)
    print("\nAll Cyber Incidents:")
    incidents_df = get_all_incidents(conn)
    print(incidents_df)

    # Update incident status
    update_incident_status(conn, 1000, 'Resolved')
    print("\nUpdated Incident Status:")
    incidents_df = get_all_incidents(conn)
    print(incidents_df)

    # Delete an incident
    delete_incident(conn, 1010)
    print("\nIncidents after Deletion:")
    incidents_df = get_all_incidents(conn)
    print(incidents_df)

    # Create dataset metadata
    create_dataset_metadata(conn, 'Sales_Data', 1000, 10, 'Charlie', '2024-06-01')
    print("\nInserted Dataset Metadata:")
    inserted_dataset = get_all_datasets_metadata(conn)
    print(inserted_dataset)

    # Retrieve and display all dataset metadata
    get_all_datasets_metadata(conn)
    print("\nAll Dataset Metadata:")
    datasets_df = get_all_datasets_metadata(conn)
    print(datasets_df)

    # Update dataset uploaded_by
    update_dataset_uploaded_by(conn, 1, 'Dave')
    print("\nUpdated Dataset Uploaded By:")
    datasets_df = get_all_datasets_metadata(conn)
    print(datasets_df)

    # Delete dataset metadata
    delete_dataset_metadata(conn, 2)
    print("\nDatasets after Deletion:")
    datasets_df = get_all_datasets_metadata(conn)
    print(datasets_df)

    # Insert a ticket
    insert_ticket('High', 'System crash on login', 'Open', 'Alice', '2024-06-01 10:00:00.000000', 48)
    print("\nInserted Ticket:")
    inserted_ticket = get_all_tickets()
    print(inserted_ticket)

    # Retrieve and display all tickets
    tickets_df = get_all_tickets()
    print("\nAll Tickets:")
    print(tickets_df)

    # Update ticket status
    update_ticket_status(2002, 'Resolved')
    print("\nUpdated Ticket Status:")
    tickets_df = get_all_tickets()
    print(tickets_df)

    # Delete a ticket
    delete_ticket(2001)
    print("\nTickets after Deletion:")
    tickets_df = get_all_tickets()
    print(tickets_df)

    # Save changes
    conn.commit()

    # Close the database connection
    conn.close()

# Run the main function
if __name__ == "__main__":
    main()




