import sqlite3
from app.data.db import connect_database

def insert_user(username, password_hash, role):
    """
    Insert a new user into the database.

    Args:
        username (str): The username of the user.
        password_hash (str): The hashed password of the user.
        role (str): The role of the user (default is 'user').
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
        (username, password_hash, role)
    )
    conn.commit()
    conn.close()

def get_user_by_username(username):
    """
    Retrieve a user by username.

    Args:
        username (str): The username of the user.
    
    Returns:
        tuple: The user record, or None if not found.
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def update_user_role(username, new_role):
    """
    Update the role of a user.

    Args:
        username (str): The username of the user.
        new_role (str): The new role to assign to the user.
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET role = ? WHERE username = ?", (new_role, username))
    conn.commit()
    conn.close()

def delete_user(username):
    """
    Delete a user from the database.

    Args:
        username (str): The username of the user to delete.
    """
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()



