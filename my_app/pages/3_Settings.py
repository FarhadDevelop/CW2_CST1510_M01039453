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

st.header("Account Settings")
st.text_input("Username", value=st.session_state.username)
st.text_input("Email", value="")
st.text_input("Role", value=st.session_state.role)
st.button("Update Settings")
if st.button("Update Settings"):
    st.success("Settings updated successfully!")


