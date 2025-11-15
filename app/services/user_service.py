import sqlite3
import bcrypt
from pathlib import Path
from app.data.db import connect_database

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

def migrate_users_from_file(conn, filepath=DATA_DIR / "users.txt"):
    """
    Migrate users from a text file to the database.

    Args:
        conn (sqlite3.Connection): The database connection.
        filepath (str or Path): The path to the user data file.
    
    Returns:
        int: The number of users migrated.
    """
    path = Path(filepath)
    
    # Check if file exists
    if not path.exists():
        print(f"Warning: {filepath} not found. Skipping migration.")
        return 0
    
    cursor = conn.cursor()
    migrated_count = 0
    
    # Read the file line by line
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            
            # Skip empty lines and comments
            if not line or line.startswith("#"):
                continue
            
            # Parse the line
            parts = [p.strip() for p in line.split(",")]
            if len(parts) < 2:
                continue
            
            username = parts[0]
            password_hash = parts[1]
            role = parts[2] if len(parts) >= 3 else "user"
            
            # Insert into database using parameterized query
            try:
                cursor.execute(
                    "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                    (username, password_hash, role)
                )
                migrated_count += 1
            except sqlite3.IntegrityError:
                # User already exists (username is UNIQUE)
                print(f" User '{username}' already exists. Skipping.")
    
    conn.commit()
    return migrated_count

