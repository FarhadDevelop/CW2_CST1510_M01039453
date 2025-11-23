import streamlit as st

# Page configuration
set_page_config = st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="centered"
)

# Initialize session state variables if they don't exist
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = "user"

# Guard: if not logged in, redirect to Home page
if not st.session_state.logged_in:
    st.error("You must be logged in to view the settings.")
    if st.button("Go to login page"):
        st.switch_page("Home.py")  # back to the first page
    st.stop()

# Settings Page Content
st.title("⚙️ Settings")
st.write("Adjust your application settings here.")

# Display current user information
st.subheader("User Information")
st.write(f"**Username:** {st.session_state.username}")
st.write(f"**Role:** {st.session_state.role}")

# Allow user to update their username
new_username = st.text_input("Update Username", value=st.session_state.username)
if st.button("Update Username"):
    st.session_state.username = new_username
    st.success("Username updated successfully!")
    st.rerun()

# Allow user to update their role
new_role = st.selectbox("Update Role", options=["user", "admin"], index=["user", "admin"].index(st.session_state.role))
if st.button("Update Role"):
    st.session_state.role = new_role
    st.success("Role updated successfully!")
    st.rerun()

# Logout button
st.divider()
if st.button("Log out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = "user"
    st.success("You have been logged out.")
    st.switch_page("Home.py")  # Redirect to Home page after logout



