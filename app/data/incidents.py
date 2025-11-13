import sqlite3
import pandas as pd
from app.data.db import connect_database

def insert_incident(conn, timestamp, category, severity, status, description):
    """Insert a new incident into the incidents table."""
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cyber_incidents (timestamp, category, severity, status, description)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, category, severity, status, description))
    
    conn.commit()
    return cursor.lastrowid

def get_all_incidents(conn):
    """Retrieve all incidents from the database."""
    query = "SELECT * FROM cyber_incidents ORDER BY incident_id"
    df = pd.read_sql_query(query, conn)
    return df

def get_incidents_by_severity(conn, severity):
    """Retrieve incidents filtered by severity."""
    query = "SELECT * FROM cyber_incidents WHERE severity = ? ORDER BY incident_id"
    df = pd.read_sql_query(query, conn, params=(severity,))
    return df

def get_incidents_by_status(conn, status):
    """Retrieve incidents filtered by status."""
    query = "SELECT * FROM cyber_incidents WHERE status = ? ORDER BY incident_id"
    df = pd.read_sql_query(query, conn, params=(status,))
    return df

def update_incident_status(conn, incident_id, new_status):
    """Update the status of an incident."""
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE cyber_incidents SET status = ? WHERE incident_id = ?",
        (new_status, incident_id)
    )
    
    conn.commit()
    rows_affected = cursor.rowcount
    
    if rows_affected > 0:
        print(f"✅ Incident #{incident_id} status updated to '{new_status}'.")
        return True
    else:
        print(f"⚠️ No incident found with ID {incident_id}.")
        return False

def delete_incident(conn, incident_id):
    """Delete an incident from the database."""
    cursor = conn.cursor()
    
    cursor.execute(
        "DELETE FROM cyber_incidents WHERE incident_id = ?",
        (incident_id,)
    )
    
    conn.commit()
    rows_affected = cursor.rowcount
    
    if rows_affected > 0:
        print(f" Incident #{incident_id} deleted successfully.")
        return True
    else:
        print(f"No incident found with ID {incident_id}.")
        return False









