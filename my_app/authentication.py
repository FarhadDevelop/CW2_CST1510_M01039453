import streamlit as st
import bcrypt
from database import DatabaseManager

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
            st.success("Login successful!")
            st.switch_page("CW2_CST1510_M01039453/my_app/pages/1_Dashboard.py")
        else:
            st.error("Invalid credentials")
    else:
        st.error("Please enter both username and password")
