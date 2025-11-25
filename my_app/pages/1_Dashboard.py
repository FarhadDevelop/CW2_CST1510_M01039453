import streamlit as st
from data.db import connect_database
from database import DatabaseManager
from data.incidents import get_all_incidents, get_incidents_by_severity, get_incidents_by_status, insert_incident, update_incident_status, delete_incident
from data.datasets import get_all_datasets_metadata, create_dataset_metadata, update_dataset_rows, delete_dataset_metadata
from data.tickets import get_all_tickets, insert_ticket, update_ticket_status, delete_ticket

# Set page configuration
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

# Initialize database manager
db_manager = DatabaseManager("CW2_CST1510_M01039453/DATA/intelligence_platform.db")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        st.switch_page("Home.py")      # back to the first page
    st.stop()

# Connect to the database
conn = connect_database()

# Dashboard title with icon and welcome message
st.title("📊 Multi-Domain Intelligence Platform Dashboard")
st.success(f"Hello, **{st.session_state.username}**! You are logged in as **{st.session_state.role}**.")

# Domain selection
domain = st.selectbox("Select Domain", ["Cybersecurity", "Data Science", "IT"])

# Depending on the selected domain, show relevant functionalities
if domain == "Cybersecurity":
    st.header("Cybersecurity Incident Management")
    incidents = get_all_incidents(conn)
    st.dataframe(incidents)
    # Add more incident management functionalities here (CRUD operations) but only for admin
    if st.session_state.role != "admin":
        st.warning("You do not have permission to modify incidents.")
    else:
        st.subheader("Add New Incident")
        with st.form("add_incident_form"):
            # Combine date and time inputs into a single timestamp
            date = st.date_input("Date")
            time = st.time_input("Time")
            timestamp = f"{date} {time}"
        
            category = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
            severity = st.selectbox("Category", ["Phishing", "Malware", "DDoS", "Misconfiguration", "Unauthorized Access"])
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
            description = st.text_area("Description")
            submitted = st.form_submit_button("Add Incident")   

            if submitted:
                insert_incident(conn, timestamp, category, severity, status, description)
                st.success("Incident added successfully.")
                st.rerun()
    
        st.subheader("Filter Incidents")
        with st.form("filter_incidents_form"):
            severity_filter = st.selectbox("Filter by Severity", ["Low", "Medium", "High", "Critical"])
            status_filter = st.selectbox("Filter by Status", ["Open", "In Progress", "Resolved", "Closed"])
            submitted = st.form_submit_button("Apply Filters")
        
        if submitted:
            severity_filtered = get_incidents_by_severity(conn, severity_filter)
            status_filtered = get_incidents_by_status(conn, status_filter)
            filtered_incidents = severity_filtered.merge(status_filtered)
            st.dataframe(filtered_incidents)

        st.subheader("Update Incident Status")
        with st.form("update_incident_form"):
            incident_id = st.number_input("Incident ID", min_value=1)
            new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved", "Closed"])
            submitted = st.form_submit_button("Update Status")
        
        if submitted:
            update_incident_status(conn, incident_id, new_status)
            st.success("Incident status updated successfully.")
            st.rerun()
    
        st.subheader("Delete Incident")
        with st.form("delete_incident_form"):
            incident_id_del = st.number_input("Incident ID to Delete", min_value=1)
            submitted = st.form_submit_button("Delete Incident")

        if submitted:
            delete_incident(conn, incident_id_del)
            st.success("Incident deleted successfully.")
            st.rerun()

if domain == "Data Science":
    st.header("Dataset Management")
    datasets = get_all_datasets_metadata(conn)
    st.dataframe(datasets)
    # Add more dataset management functionalities here (CRUD operations) but only for admin
    if st.session_state.role != "admin":
        st.warning("You do not have permission to modify dataset metadata.")
    else:
        st.subheader("Add New Dataset Metadata")
        with st.form("add_dataset_form"):
            name = st.text_input("Dataset Name")
            num_rows = st.number_input("Number of Rows", min_value=0)
            num_columns = st.number_input("Number of Columns", min_value=0)
            uploaded_by = st.selectbox("Uploaded By", ["data_scientist (Alice Smith)", "it_admin (Carol Lee)", "cyber_analyst (Bob Johnson)"])
            upload_date = st.date_input("Upload Date")
            submitted = st.form_submit_button("Add Dataset Metadata")

        if submitted:
            create_dataset_metadata(conn, name, num_rows, num_columns, uploaded_by, upload_date)
            st.success("Dataset metadata added successfully.")
            st.rerun()
    
        st.subheader("Update Dataset Rows")
        with st.form("update_dataset_form"):
            dataset_id = st.number_input("Dataset ID", min_value=1)
            new_num_rows = st.number_input("New Number of Rows", min_value=0)
            submitted = st.form_submit_button("Update Dataset Rows")

        if submitted:
            update_dataset_rows(conn, dataset_id, new_num_rows)
            st.success("Dataset rows updated successfully.")
            st.rerun()
    
        st.subheader("Delete Dataset Metadata")
        with st.form("delete_dataset_form"):
            dataset_id_del = st.number_input("Dataset ID to Delete", min_value=1)
            submitted = st.form_submit_button("Delete Dataset Metadata")

        if submitted:
            delete_dataset_metadata(conn, dataset_id_del)
            st.success("Dataset metadata deleted successfully.")
            st.rerun()

if domain == "IT":
    st.header("IT Ticket Management")
    tickets = get_all_tickets()
    st.dataframe(tickets)
    # Add more ticket management functionalities here (CRUD operations) but only for admin
    if st.session_state.role != "admin":
        st.warning("You do not have permission to modify tickets.")
    else:
        st.subheader("Create New Ticket")
        with st.form("create_ticket_form"):
            priority = st.selectbox("Priority", ["Low", "Medium", "High", "Critical"])
            description = st.text_area("Description")
            status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
            assigned_to = st.selectbox("Assigned To", ["IT_Support_A (Alice Smith)", "IT_Support_B (Bob Johnson)", "IT_Admin (Charlie Lee)"])
        
        # Combine date and time inputs into a single timestamp
            date = st.date_input("Date")
            time = st.time_input("Time")
            created_at = f"{date} {time}"
            
            resolution_time_hours = st.number_input("Estimated Resolution Time (hours)", min_value=0)
            submitted = st.form_submit_button("Create Ticket")

        if submitted and description:
            insert_ticket(conn, priority, description, status, assigned_to, created_at, resolution_time_hours)
            st.success("Ticket created successfully.")
            st.rerun()
    
        st.subheader("Update Ticket Status")
        with st.form("update_ticket_form"):
            ticket_id = st.number_input("Ticket ID", min_value=1)
            new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved", "Closed"])
            submitted = st.form_submit_button("Update Ticket Status")
        if submitted:
            update_ticket_status(conn, ticket_id, new_status)
            st.success("Ticket status updated successfully.")
            st.rerun()
    
        st.subheader("Delete Ticket")
        with st.form("delete_ticket_form"):
            ticket_id_del = st.number_input("Ticket ID to Delete", min_value=1)
            submitted = st.form_submit_button("Delete Ticket")

        if submitted:
            delete_ticket(conn, ticket_id_del)
            st.success("Ticket deleted successfully.")
            st.rerun()

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.switch_page("Home.py")