import streamlit as st
from data.db import connect_database
from data.incidents import get_all_incidents, get_incidents_by_severity, get_incidents_by_status, insert_incident, update_incident_status, delete_incident
from data.datasets import get_all_datasets_metadata, create_dataset_metadata, update_dataset_rows
from data.tickets import get_all_tickets, insert_ticket, update_ticket_status, delete_ticket

st.set_page_config(page_title="Dashboard", layout="wide")

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

# If logged in, show user info and dashboard.
st.title("Multi-Domain Intelligence Platform")
st.success(f"Hello, **{st.session_state.username}**! You are logged in as **{st.session_state.role}**.")

# Domain selection
domain = st.selectbox("Select Domain", ["Cybersecurity", "Data Science", "IT"])

# Depending on the selected domain, show relevant functionalities
if domain == "Cybersecurity":
    st.header("Cybersecurity Incident Management")
    incidents = get_all_incidents(conn)
    st.dataframe(incidents)
    # Add more incident management functionalities here (CRUD operations)
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

if domain == "Data Science":
    st.header("Dataset Management")
    datasets = get_all_datasets_metadata(conn)
    st.dataframe(datasets)
    # Add more dataset management functionalities here (CRUD operations)
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

if domain == "IT":
    st.header("IT Ticket Management")
    tickets = get_all_tickets()
    st.dataframe(tickets)
    # Add more ticket management functionalities here (CRUD operations)
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

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.switch_page("Home.py")