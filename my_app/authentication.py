import streamlit as st
import bcrypt
from database import DatabaseManager

# Initialize database
db = DatabaseManager("CW2_CST1510_M01039453/DATA/intelligence_platform.db")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in"):
    # Hash the entered password
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # Verify with database
    if db.verify_user(username, password_hash):
        st.session_state.logged_in = True
        st.session_state.username = username
        st.switch_page("pages/1_Dashboard.py")
    else:
        st.error("Invalid credentials")
