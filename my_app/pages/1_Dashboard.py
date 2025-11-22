import streamlit as st
from data.db import connect_database
from data.incidents import get_all_incidents, insert_incident

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

# READ: Display all incidents in a table
incidents = get_all_incidents(conn)
st.subheader("All Reported Cyber Incidents")
st.dataframe(incidents, use_container_width=True)

# CREATE: Form to add a new incident
st.subheader("Report a New Cyber Incident")
with st.form("new_incident"):
    timestamp = st.text_input("Timestamp (YYYY-MM-DD HH:MM:SS.ffffff)")
    category = st.selectbox("Category", ["Phishing", "Malware", "Misconfiguration", "DDoS", "Unauthorized Access"])
    severity = st.selectbox("Severity", ["Low", "Medium", "High", "Critical"])
    status = st.selectbox("Status", ["Open", "In Progress", "Resolved", "Closed"])
    description = st.text_input("Description")

    # Form submit button
    submitted = st.form_submit_button("Report Incident")

    # Handle form submission
    if submitted:
        insert_incident(conn, timestamp, category, severity, status, description)
        st.success("New incident reported successfully!")
        st.rerun()  # Refresh the page to show the new incident

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = ""
    st.success("You have been logged out.")
    st.switch_page("Home.py")