import sqlite3
import pandas as pd
from app.data.db import connect_database
from pathlib import Path

DATA_DIR = Path("CW2_CST1510_M01039453/DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

def insert_ticket(priority, description, status, assigned_to, created_at, resolution_time_hours):
    conn = connect_database(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tickets (priority, description, status, assigned_to, created_at, resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (priority, description, status, assigned_to, created_at, resolution_time_hours))
    conn.commit()
    conn.close()

def get_all_tickets():
    conn = connect_database(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM tickets", conn)
    conn.close()
    return df

def update_ticket_status(ticket_id, new_status):
    conn = connect_database(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tickets
        SET status = ?
        WHERE ticket_id = ?
    """, (new_status, ticket_id))
    conn.commit()
    conn.close()

def delete_ticket(ticket_id):
    conn = connect_database(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE ticket_id = ?", (ticket_id,))
    
    conn.commit()
    conn.close()