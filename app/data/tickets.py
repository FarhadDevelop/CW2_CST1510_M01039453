def insert_ticket(ticket_data):
    conn = connect_database(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO tickets (ticket_id, priority, description, status, assigned_to, created_at, resolution_time_hours)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket_data['ticket_id'],
        ticket_data['priority'],
        ticket_data['description'],
        ticket_data['status'],
        ticket_data['assigned_to'],
        ticket_data['created_at'],
        ticket_data['resolution_time_hours']
    ))
    conn.commit()
    conn.close()

def get_all_tickets():
    conn = connect_database(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM tickets", conn)
    conn.close()
    return df

def update_ticket(ticket_id, update_data):
    conn = connect_database(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE tickets
        SET priority = ?, description = ?, status = ?, assigned_to = ?, created_at = ?, resolution_time_hours = ?
        WHERE ticket_id = ?
    """, (
        update_data['priority'],
        update_data['description'],
        update_data['status'],
        update_data['assigned_to'],
        update_data['created_at'],
        update_data['resolution_time_hours'],
        ticket_id
    ))
    conn.commit()
    conn.close()

def delete_ticket(ticket_id):
    conn = connect_database(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tickets WHERE ticket_id = ?", (ticket_id,))
    
    conn.commit()
    conn.close()