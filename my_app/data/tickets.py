import sqlite3
import pandas as pd
from data.db import connect_database

def insert_ticket(priority, description, status, assigned_to, created_at, resolution_time_hours):
    """
    Insert a new IT ticket into the database.

    Args:
        priority (str): The priority of the ticket.
        description (str): The description of the ticket.
        status (str): The status of the ticket.
        assigned_to (str): The person assigned to the ticket.
        created_at (str): The creation timestamp of the ticket.
        resolution_time_hours (int): The resolution time in hours.
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO it_tickets (priority, description, status, assigned_to, created_at, resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (priority, description, status, assigned_to, created_at, resolution_time_hours))
    conn.commit()
    conn.close()

def get_all_tickets():
    """
    Retrieve all IT tickets from the database.

    Returns:
        pandas.DataFrame: A DataFrame containing all IT tickets.
    """
    conn = connect_database()
    df = pd.read_sql_query("SELECT * FROM it_tickets", conn)
    conn.close()
    return df

def update_ticket_status(ticket_id, new_status):
    """
    Update the status of an IT ticket.

    Args:
        ticket_id (int): The ID of the ticket to update.
        new_status (str): The new status to set.
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE it_tickets
        SET status = ?
        WHERE ticket_id = ?
    """, (new_status, ticket_id))
    conn.commit()
    conn.close()

def delete_ticket(ticket_id):
    """
    Delete an IT ticket from the database.

    Args:
        ticket_id (int): The ID of the ticket to delete.
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM it_tickets WHERE ticket_id = ?", (ticket_id,))
    
    conn.commit()
    conn.close()