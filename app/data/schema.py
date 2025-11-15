def create_users_table(conn):
    """
    Create the users table.

    Args:
        conn (sqlite3.Connection): The database connection.
    """
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
    """
    Create the cyber_incidents table.
    
    Args:
        conn (sqlite3.Connection): The database connection.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS cyber_incidents (
        incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        description TEXT NOT NULL,
        severity TEXT NOT NULL,
        category TEXT,
        status TEXT DEFAULT 'open'
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("Cyber incidents table created successfully.")

def create_datasets_metadata_table(conn):
    """
    Create the datasets_metadata table.

    Args:
        conn (sqlite3.Connection): The database connection.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS datasets_metadata (
        dataset_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        rows INTEGER,
        columns INTEGER,
        uploaded_by TEXT,
        upload_date TEXT
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("Datasets metadata table created successfully.")

def create_it_tickets_table(conn):
    """
    Create the it_tickets table.

    Args:
        conn (sqlite3.Connection): The database connection.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS it_tickets (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        priority TEXT NOT NULL,
        description TEXT NOT NULL,
        status TEXT DEFAULT 'open',
        assigned_to TEXT,
        created_at TEXT NOT NULL,
        resolution_time_hours INTEGER
    );
    """

    cursor = conn.cursor()
    cursor.execute(create_table_sql)
    conn.commit()
    print("IT tickets table created successfully.")

def create_all_tables(conn):
    """
    Create all necessary tables in the database.

    Args:
        conn (sqlite3.Connection): The database connection.
    """
    create_users_table(conn)
    create_cyber_incidents_table(conn)
    create_datasets_metadata_table(conn)
    create_it_tickets_table(conn)
    print("\nAll tables created successfully.")











    





