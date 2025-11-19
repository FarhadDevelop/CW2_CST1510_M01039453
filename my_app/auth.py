import streamlit as st
import bcrypt
from database import DatabaseManager

# Initialize database
db = DatabaseManager("DATA/intelligence_platform.db")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in"):
    # Hash the password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Verify with database
if db.verify_user(username, password_hash):
    st.session_state.logged_in = True
    st.session_state.username = username
    st.session_state.role = db.get_user_role(username)
    st.switch_page("pages/1_Dashboard.py")
else:
    st.error("Invalid credentials")