# CW2 for module CST1510
Final project for module CST1510 involving developing a substantial Streamlit application incorporating Data Science, Cyber Security, and IT

# Week 7: Secure Authentication System
- Student Name: Farhad Binu Manaf
- Student ID: M01039453
- Course: CST1510 - CW2 - Multi-Domain Intelligence Platform

## Project Description
A command-line authentication system implementing secure password hashing. This system allows users to register accounts and log in using securely hashed passwords with `bcrypt`.

## Features
- Secure password hashing using bcrypt with automatic salt generation
- User registration with duplicate username prevention
- User login with password verification
- Input validation for usernames and passwords
- File-based user data persistence

## Technical Implementation
- Hashing Algorithm: bcrypt with automatic salting
- Data Storage: Plain text file (`users.txt`) with comma-separated values
- Password Security: One-way hashing, no plaintext storage
- Validation: Username (3-20 alphanumeric characters), Password (6-50 characters)

# Week 8: Database Layer
- Student Name: Farhad Binu Manaf
- Student ID: M01039453
- Course: CST1510 - CW2 - Multi-Domain Intelligence Platform

## Project Description
Implementation of a persistent SQLite database layer to manage multi-domain intelligence data (users, cyber incidents, datasets metadata, IT tickets). The database layer provides schema creation, migration from legacy file storage, bulk CSV imports, and programmatic CRUD operations used by the application.

## Features
- SQLite database
- Database connection helper for consistent connections
- Schema creation utilities to create all required tables programmatically
- Migration of file-based users (`users.txt`) into the users table
- Bulk CSV import for three domains using pandas
- CRUD operations for each domain
- Quick data inspection via `pandas.read_sql_query` for tabular output and verification

## Technical Implementation
- Database: SQLite file at DATA folder
- Connection helper: `app.data.db.connect_database()` — wraps sqlite3.connect with a canonical DB path
- Schema creation: `app.data.schema` contains functions that create tables
- User migration: `app.services.user_service.migrate_users_from_file(conn, filepath=DATA_DIR / "users.txt")` reads `users.txt` (skips comments/empty lines), parses CSV fields, and inserts parameterized rows into the users table (handles UNIQUE conflicts)
- Passwords: bcrypt hashing used in app.services.user_service.register_user and login_user (no plaintext stored)
- CSV loading: `main.load_csv_to_table` reads each CSV with pandas, cleans column names, and uses `df.to_sql(..., if_exists='append', index=False)` to load rows into the matching tables
- Data access packages: Each domain has a focused module (`app.data.users`, `app.data.incidents`, `app.data.datasets`, `app.data.tickets`) exposing small, testable functions to perform CRUD operations and return results (rows, dataframes, or boolean status)
- Utilities & examples: `main.py` demonstrates end-to-end usage — connect, create tables, migrate users, import CSVs, insert/update/delete records, and print tables for verification using pandas