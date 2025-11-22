import streamlit as st
from data.db import connect_database
from data.incidents import get_all_incidents, insert_incident, update_incident_status, delete_incident

st.set_page_config(page_title="Cyber Incidents Dashboard", layout="wide")

# Ensure state keys exist (in case user opens this page first)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = "user"

# Guard: if not logged in, send user back
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")
    if st.button("Go to login page"):
        st.switch_page("Home.py")      # back to the first page
    st.stop()

# Connect to the database
conn = connect_database()

# If logged in, show user info and dashboard.
st.title("Cyber Incidents Dashboard")
st.success(f"Hello, **{st.session_state.username}**! You are logged in as **{st.session_state.role}**.")

# Tabs for different functionalities
tab_1, tab_2, tab_3, tab_4 = st.tabs(["View Incidents", "Add Incident", "Manage Incidents", "Delete Incident"])

# VIEW: Display all incidents in tab 1
with tab_1:
    st.header("View All Cyber Incidents")
    incidents = get_all_incidents(conn)
    st.dataframe(incidents, use_container_width=True)

# CREATE: Form to add a new incident in tab 2
with tab_2:
    st.header("Report a New Cyber Incident")
    with st.form("new_incident_form"):
        timestamp = st.text_input("Timestamp (YYYY-MM-DD HH:MM:SS.ffffff)")
        category = st.selectbox("Category", ["Phishing", "Malware", "Misconfiguration", "DDoS", "Unauthorized Access"])
        severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
        status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
        description = st.text_input("Description")

        submitted = st.form_submit_button("Report Incident")

        if submitted:
            insert_incident(conn, timestamp, category, severity, status, description)
            st.success("New incident reported successfully!")
            st.rerun()  # Refresh the page to show the new incident

# UPDATE: Form to update an existing incident status in tab 3
with tab_3:
    st.header("Manage Existing Cyber Incidents")

    # UPDATE: Form to update an existing incident status
    st.subheader("Update an Existing Incident Status")
    with st.form("update_incident_form"):
        incidents = get_all_incidents(conn)
        incident_ids = incidents['incident_id'].tolist()
        incident_id = st.selectbox("Select Incident ID", incident_ids)
        new_status = st.selectbox("New Status", ["Open", "In Progress", "Resolved", "Closed"])

        update_submitted = st.form_submit_button("Update Status")

        if update_submitted:
            update_incident_status(conn, incident_id, new_status)
            st.success(f"Incident ID {incident_id} status updated successfully to {new_status}!")
            st.rerun()  # Refresh the page to show the updated status

# DELETE: Form to delete an incident in tab 4
with tab_4:
    st.header("Delete a Cyber Incident")
    with st.form("delete_incident_form"):
        incidents = get_all_incidents(conn)
        incident_ids = incidents['incident_id'].tolist()
        incident_id_to_delete = st.selectbox("Select Incident ID to Delete", incident_ids)

        delete_submitted = st.form_submit_button("Delete Incident")

        if delete_submitted:
            delete_incident(conn, incident_id_to_delete)
            st.success(f"Incident ID {incident_id_to_delete} deleted successfully!")
            st.rerun()  # Refresh the page to show the updated incidents

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.switch_page("Home.py")