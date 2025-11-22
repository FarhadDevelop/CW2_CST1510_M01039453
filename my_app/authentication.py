import streamlit as st
import bcrypt
from database import DatabaseManager

# Set page config
st.set_page_config(page_title="Login", page_icon="🔐")
st.title("🔐 Login")

# Initialize session state (in case of direct access)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ""
if 'role' not in st.session_state:
    st.session_state.role = ""

# If already logged in, go straight to dashboard
if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}**.")
    if st.button("Go to Dashboard"):
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

# Initialize database
db = DatabaseManager("CW2_CST1510_M01039453/DATA/intelligence_platform.db")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in"):
    if username and password:
        # Get stored hash from database
        stored_hash = db.get_user_password_hash(username)
        # Verify password
        if stored_hash and bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8')):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = db.get_user_role(username)
            st.success("Login successful!")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials")
    else:
        st.error("Please enter both username and password")
