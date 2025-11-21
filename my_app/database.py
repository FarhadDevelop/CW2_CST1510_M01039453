import sqlite3
import streamlit as st

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_user_password_hash(self, username):
        """Get user password hash from database"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,)
            )
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else None
        except sqlite3.Error as e:
            st.error(f"Database error: {e}")
        finally:
            conn.close()
    

    def get_user_role(self, username):
        """Get user role from database"""
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT role FROM users WHERE username = ?", (username,)
            )
            result = cursor.fetchone()
            conn.close()
            return result[0] if result else None
        except sqlite3.Error as e:
            st.error(f"Database error: {e}")
        finally:
            conn.close()