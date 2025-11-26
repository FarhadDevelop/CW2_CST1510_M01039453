import streamlit as st
from data.users import update_user_role, delete_user

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
st.write("Adjust your account settings here.")

# Display current user information
st.subheader("User Information")
st.write(f"**Username:** {st.session_state.username}")
st.write(f"**Role:** {st.session_state.role}")

# Allow user to update their role
new_role = st.selectbox("Update Role", options=["user", "admin"], index=["user", "admin"].index(st.session_state.role))
if st.button("Update Role"):
    update_user_role(st.session_state.username, new_role)
    st.session_state.role = new_role
    st.success("Role updated successfully!")
    st.rerun()

# Allow user to delete their account
st.divider()
st.subheader("Delete Account")
st.write("Warning: This action is irreversible.")
if st.button("Delete Account"):
    delete_user(st.session_state.username)
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.role = "user"
    st.success("Your account has been deleted.")
    st.switch_page("Home.py")  # Redirect to Home page after deletion





