import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def verify_user(self, username, password_hash):
        """Verify user credentials"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", 
                       (username, password_hash)
                       )
        
        user = cursor.fetchone()
        conn.close()

        return user is not None

    def get_user_role(self, username):
        """Get user role from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("SELECT role FROM users WHERE username = ?", (username,)
        )

        result = cursor.fetchone()
        conn.close()

        return result[0] if result else None