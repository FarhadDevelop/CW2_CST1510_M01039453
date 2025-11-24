import sqlite3
import bcrypt
from pathlib import Path
from data.db import connect_database

# Define the path to the database
DATA_DIR = Path("CW2_CST1510_M01039453/DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

def register_user(username, password, role="user"):
    """ 
    Register a new user in the database.
    
    Args:
        username (str): The desired username.
        password (str): The plain text password.
        role (str): The role of the user (default is "user").
    
    Returns:
        tuple: (bool, str) indicating success status and message.
    """
    # Validate input
    if not username or not password:
        return False, "Username and password are required."
    
    conn = connect_database()
    cursor = conn.cursor()
    
    # Check if username already exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        conn.close()
        return False, f"Username '{username}' already exists."
    
    # Hash the password
    password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    password_hash_str = password_hash.decode("utf-8")
    
    # Insert new user
    cursor.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash_str, role)
    )
    conn.commit()
    conn.close()
    
    return True, f"User '{username}' registered successfully with role '{role}'."

def login_user(username, password):
    """
    Authenticate a user with the given username and password.
    
    Args:
        username (str): The username of the user.
        password (str): The plain text password of the user.

    Returns:
        tuple: (bool, str) indicating success status and message.
    """
    conn = connect_database()
    cursor = conn.cursor()
    
    # Look up user
    cursor.execute(
        "SELECT password_hash, role FROM users WHERE username = ?",
        (username,)
    )
    row = cursor.fetchone()
    conn.close()
    
    # User not found
    if not row:
        return False, "User not found."
    
    stored_hash, role = row
    
    # Verify password
    if bcrypt.checkpw(password.encode("utf-8"), stored_hash.encode("utf-8")):
        return True, f"Login successful! Welcome {username} (role: {role})."
    else:
        return False, "Incorrect password."


