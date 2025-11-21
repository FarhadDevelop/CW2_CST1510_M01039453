import sqlite3
import pandas as pd
from data.db import connect_database

def insert_incident(conn, timestamp, category, severity, status, description):
    """
    Insert a new incident into the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        timestamp (str): The timestamp of the incident.
        category (str): The category of the incident.
        severity (str): The severity level of the incident.
        status (str): The current status of the incident.
        description (str): A description of the incident.
    
    Returns:
        int: The ID of the newly inserted incident.
    """
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO cyber_incidents (timestamp, category, severity, status, description)
        VALUES (?, ?, ?, ?, ?)
    """, (timestamp, category, severity, status, description))
    
    conn.commit()
    return cursor.lastrowid

def get_all_incidents(conn):
    """
    Retrieve all incidents from the database.

    Args:
        conn (sqlite3.Connection): The database connection.
    
    Returns:
        pd.DataFrame: A DataFrame containing all incidents.
    """
    query = "SELECT * FROM cyber_incidents ORDER BY incident_id"
    df = pd.read_sql_query(query, conn)
    return df

def get_incidents_by_severity(conn, severity):
    """
    Retrieve incidents filtered by severity.

    Args:
        conn (sqlite3.Connection): The database connection.
        severity (str): The severity level to filter by.
    
    Returns:
        pd.DataFrame: A DataFrame containing incidents with the specified severity.
    """
    query = "SELECT * FROM cyber_incidents WHERE severity = ? ORDER BY incident_id"
    df = pd.read_sql_query(query, conn, params=(severity,))
    return df

def get_incidents_by_status(conn, status):
    """
    Retrieve incidents filtered by status.

    Args:
        conn (sqlite3.Connection): The database connection.
        status (str): The status to filter by.
    
    Returns:
        pd.DataFrame: A DataFrame containing incidents with the specified status.
    """
    query = "SELECT * FROM cyber_incidents WHERE status = ? ORDER BY incident_id"
    df = pd.read_sql_query(query, conn, params=(status,))
    return df

def update_incident_status(conn, incident_id, new_status):
    """
    Update the status of an incident.

    Args:
        conn (sqlite3.Connection): The database connection.
        incident_id (int): The ID of the incident to update.
        new_status (str): The new status to set.
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
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
    """
    Delete an incident from the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        incident_id (int): The ID of the incident to delete.
    
    Returns:
        bool: True if the deletion was successful, False otherwise.
    """
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









