import sqlite3
from pathlib import Path

# Define the path to the database
DATA_DIR = Path("CW2_CST1510_M01039453/DATA")
DB_PATH = DATA_DIR / "intelligence_platform.db"

def migrate_users_from_file(conn, filepath=DATA_DIR / "users.txt"):
    """Migrate users from users.txt to the database."""
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

