import streamlit as st
import bcrypt
from database import DatabaseManager
from authentication import register_user, login_user

# Set page configuration
st.set_page_config(page_title="Login / Register", page_icon="🔑", layout="centered")

# Initialise session state
if "users" not in st.session_state:
    st.session_state["users"] = {}

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

if "role" not in st.session_state:
    st.session_state["role"] = ""

st.title("🔐 Welcome")

# If already logged in, go straight to dashboard
if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}**.")
    if st.button("Go to Dashboard"):
        # Use Streamlit's built-in page navigation to switch to dashboard
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

# Initialize database
db = DatabaseManager("CW2_CST1510_M01039453/DATA/intelligence_platform.db")

# Tabs: Login / Register
tab_login, tab_register = st.tabs(["Login", "Register"])

# Login Tab
with tab_login:
    st.subheader("Login")

    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log in", type="primary"):
        # Validate credentials
        if login_username and login_password:
            # Get hashed password from database
            stored_hash = db.get_user_password_hash(login_username)
            if stored_hash:
                success, message = login_user(login_username, login_password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.username = login_username
                    st.session_state.role = db.get_user_role(login_username)
                    st.success(f"Welcome back, {login_username}!")
                    st.info(message)
                    # Redirect to dashboard page
                    st.switch_page("pages/1_Dashboard.py")

            users = st.session_state.users
        if login_username in users and users[login_username] == login_password:
            st.session_state.logged_in = True
            st.session_state.username = login_username
            st.session_state.role = db.get_user_role(login_username)
            st.success(f"Welcome back, {login_username}!")

            # Redirect to dashboard page
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid username or password.")

# Register Tab
with tab_register:
    st.subheader("Register")

    new_username = st.text_input("Enter a username", key="register_username")
    new_password = st.text_input("Enter a password", type="password", key="register_password")
    confirm_password = st.text_input("Confirm password", type="password", key="register_confirm")
    new_role = st.selectbox("Select Role", ["user", "admin"])

    # Validation and registration
    if st.button("Create account"):
        if not new_username or not new_password:
            st.error("Username and password cannot be empty.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        elif new_username in st.session_state.users:
            st.error("Username already exists. Choose another one.")
        else:
            register_user(new_username, new_password, new_role)
            st.session_state.users[new_username] = new_password
            st.session_state["role"] = new_role
            st.success("Account created! You can now log in from the Login tab.")
            st.info("Tip: Go to the Login tab and sign in with your new account.")