import streamlit as st

st.set_page_config(page_title="Login / Register", page_icon="🔑", layout="centered")

# Initialise session state
if "users" not in st.session_state:
    st.session_state["users"] = {}

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "username" not in st.session_state:
    st.session_state["username"] = ""

st.title("🔐 Welcome")

# If already logged in, go straight to dashboard
if st.session_state.logged_in:
    st.success(f"Already logged in as **{st.session_state.username}**.")
    if st.button("Go to Dashboard"):
        # Use Streamlit's built-in page navigation to switch to dashboard
        st.switch_page("pages/1_Dashboard.py")
    st.stop()

# Tabs: Login / Register
tab_login, tab_register = st.tabs(["Login", "Register"])

# Login Tab
with tab_login:
    st.subheader("Login")

    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log in", type="primary"):
        # Validate credentials
        users = st.session_state.users
        if login_username in users and users[login_username] == login_password:
            st.session_state.logged_in = True
            st.session_state.username = login_username
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

    # Validation and registration
    if st.button("Create Account"):
        if not new_username or not new_password or not confirm_password:
            st.error("All fields are required.")
    elif new_password != confirm_password:
        st.error("Passwords do not match.")
    elif new_username in st.session_state.users:
        st.error("Username already exists. Choose another one.")
    else:
        st.session_state.users[new_username] = new_password
        st.success("Account created! You can now log in from the Login tab.")
        st.info("Tip: Go to the Login tab and sign in with your new account.")