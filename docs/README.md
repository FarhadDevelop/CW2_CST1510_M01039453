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
A SQLite-backed database layer and CSV ingestion pipeline that persist multi-domain intelligence data (cyber incidents, datasets metadata, IT tickets) and integrate the authentication/user data into the database. The main entrypoint sets up the database, migrates users from file storage, demonstrates authentication calls, and loads CSV domain data into database tables.

## Features
- SQLite database (`intelligence_platform.db`) for centralized storage
- Database schema creation and migration via `app.data.schema` and `app.services.user_service`
- User migration from legacy file-based storage into the users table
- Authentication service usage (`register_user`, `login_user`) integrated with the DB-backed users
- CSV ingestion pipeline using `pandas`: loads `cyber_incidents.csv`, `datasets_metadata.csv`, `it_tickets.csv` into corresponding tables
- CRUD operations exposed for users, incidents, datasets, and tickets via `app.data` modules
- Example data insertions, queries, updates, and deletions shown in `main.py` for testing

## Technical Implementation
- Database: SQLite accessed via `sqlite3`; database file located at DATA folder
- Schema: Tables are created by `app.data.schema.create_all_tables(conn)`
- DB Connection: Obtained through `app.data.db.connect_database()`
- CSV Loading: `pd.read_csv` reads CSVs, cleans column names, and uses `df.to_sql(..., if_exists='append', index=False)` to populate tables
- Data Files converted into Tables:
  - /DATA/cyber_incidents.csv -> table `cyber_incidents`
  - /DATA/datasets_metadata.csv -> table `datasets_metadata`
  - /DATA/it_tickets.csv -> table `it_tickets`
- Services and Modules:
  - `app.services.user_service`: `migrate_users_from_file`, `register_user`, `login_user`
  - `app.data.users`: `insert_user`, `get_user_by_username`, `update_user_role`, `delete_user`
  - `app.data.incidents`: `insert_incident`, `get_all_incidents`, `get_incidents_by_severity`, `get_incidents_by_status`, `update_incident_status`, `delete_incident`
  - `app.data.datasets`: `create_dataset_metadata`, `get_all_datasets_metadata`, `update_dataset_rows`, `delete_dataset_metadata`
  - `app.data.tickets`: `insert_ticket`, `get_all_tickets`, `update_ticket_status`, `delete_ticket`

# Week 9: UI Layer (Streamlit Interface)
- Student Name: Farhad Binu Manaf
- Student ID: M01039453
- Course: CST1510 - CW2 - Multi-Domain Intelligence Platform

## Project Description
A multi-page Streamlit application providing a user-friendly interface for secure authentication, cyber incident management, analytics, and user settings. The UI layer connects to the backend database and services, enabling interactive workflows for users and administrators.

## Features
- **Multi-page navigation** using Streamlit’s page system (`Home`, `Dashboard`, `Analytics`, `Settings`)
- **Secure login and registration** with session state management
- **Role-based access control** for user/admin features
- **Cyber Incidents Dashboard**: view, add, update, and delete incidents with real-time feedback
- **Analytics Page**: interactive metrics and visualizations (Plotly) for threat data
- **Settings Page**: view and update user profile, change role, and log out
- **Session state** persists user authentication and profile across pages
- **Logout functionality** on all pages for secure session termination

## Technical Implementation
- **Framework**: Streamlit for rapid UI development
- **Navigation**: `st.switch_page()` for page transitions; tabs for sub-features
- **Session State**: `st.session_state` stores authentication, user info, and role
- **Database Integration**: UI calls backend functions for CRUD operations (incidents, users)
- **Forms and Validation**: Streamlit forms for incident reporting, status updates, and registration
- **Visualizations**: Plotly charts for analytics (threat types, metrics)
- **Error Handling**: Guards prevent unauthorized access; feedback via `st.error`, `st.success`, etc.
- **File Structure**:
  - `Home.py`: Login and registration interface
  - `pages/1_Dashboard.py`: Incident management dashboard
  - `pages/2_Analytics.py`: Security analytics and metrics
  - `pages/3_Settings.py`: User profile and settings

