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
Introduce a SQLite-backed database layer and CSV ingestion pipeline to persist multi-domain intelligence data (cyber incidents, datasets metadata, IT tickets) and integrate the authentication/user data into the database. The main entrypoint sets up the database, migrates users from file storage, demonstrates authentication calls, and loads CSV domain data into database tables.

## Features
- SQLite database (`intelligence_platform.db`) for centralized storage
- Database schema creation and migration via app.data.schema
- User migration from legacy file-based storage into the users table
- Authentication service usage (`register_user`, `login_user`) integrated with the DB-backed users
- CSV ingestion pipeline using `pandas`: loads `cyber_incidents.csv`, `datasets_metadata.csv`, `it_tickets.csv` into corresponding tables
- CRUD operations exposed for users, incidents, datasets, and tickets via `app.data` modules
- Example data insertions, queries, updates, and deletions shown in `main.py` for testing

## Technical Implementation
- Database: SQLite accessed via `sqlite3`; database file located at DATA folder
- Schema: Tables are created by `app.data.schema.create_all_tables(conn)`
- DB Connection: Obtained through `app.data.db.connect_database()`
- CSV Loading: `pd.read_csv` reads CSVs, cleans column names, and uses `DataFrame.to_sql(..., if_exists='append', index=False)` to populate tables
- Data Files converted into Tables:
  - /DATA/cyber_incidents.csv -> table `cyber_incidents`
  - /DATA/datasets_metadata.csv -> table `datasets_metadata`
  - /DATA/it_tickets.csv -> table `it_tickets`
- Services and Modules:
  - `app.services.user_service`: `migrate_users_from_file`, `register_user`, `login_user`
  - `app.data.users`: `insert_user`, `get_user_by_username`, `update_user_role`, `delete_user`
  - `app.data.incidents`: `insert_incident`, `get_all_incidents`, `update_incident_status`, `delete_incident`
  - `app.data.datasets`: `create_dataset_metadata`, `get_all_datasets_metadata`, `update_dataset_uploaded_by`, `delete_dataset_metadata`
  - `app.data.tickets`: `insert_ticket`, `get_all_tickets`, `update_ticket_status`, `delete_ticket`
- Testing/Demo Flow (as implemented in `main.py`):
  - Connect and create tables
  - Migrate users from file into DB
  - Register and login sample user
  - Load CSV domain data into DB tables and print row counts
  - Demonstrate inserts, reads, updates, deletes for users, incidents, datasets, and tickets
  - Commit and close the database connection