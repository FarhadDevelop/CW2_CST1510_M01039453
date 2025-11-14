import sqlite3
import pandas as pd
from app.data.db import connect_database
from app.data.users import insert_user, get_user_by_username, update_user_role, delete_user
from app.data.incidents import insert_incident, get_all_incidents, update_incident_status, delete_incident
from app.data.datasets import create_dataset_metadata, get_all_datasets_metadata, update_dataset_uploaded_by, delete_dataset_metadata
from app.data.tickets import insert_ticket, get_all_tickets, update_ticket_status, delete_ticket

def main():
    """Main function to test all CRUD operations for users, cyber_incidents, datasets_metadata, and it_tickets tables in the database."""

    # Connect to the database
    conn = connect_database()

    # Insert a user
    insert_user(conn, 'bob', '$2y$10$92ns1le0rk6TUqIzxYWp/.TRQOGCoCUzm7ElT.ap06Z5dLWEZuKOS', 'analyst')
    print("\nInserted User:")
    inserted_user = get_user_by_username('bob')
    print(inserted_user)

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
    insert_incident(conn, '2024-06-01 12:00:00.000000', 'Phishing', 'High', 'Open', 'Phishing email reported by user.')
    print("\nInserted Cyber Incident:")
    inserted_incident = get_all_incidents(conn)
    print(inserted_incident)

    # Retrieve and display all incidents
    get_all_incidents(conn)
    print("\nAll Cyber Incidents:")
    incidents_df = get_all_incidents(conn)
    print(incidents_df)

    # Update incident status
    update_incident_status(conn, 1001, 'In Progress')
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
    update_ticket_status(2029, 'In Progress')
    print("\nUpdated Ticket Status:")
    tickets_df = get_all_tickets()
    print(tickets_df)

    # Delete a ticket
    delete_ticket(2001)
    print("\nTickets after Deletion:")
    tickets_df = get_all_tickets()
    print(tickets_df)

    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()




