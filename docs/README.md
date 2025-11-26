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
A multi-page Streamlit application providing a unified user interface for authentication, dashboard analytics, and CRUD management of cyber incidents, datasets, and IT tickets. The UI layer integrates with the database and authentication services, enforces role-based access control, and delivers interactive analytics and management tools for each domain.

## Features
- Streamlit-based multi-page navigation (`Home`, `Dashboard`, `Analytics`, `Settings`)
- Secure login and registration forms with password hashing and role selection
- Role-based access control: admin users can perform CRUD operations, regular users have read-only access
- Dashboard page for viewing and managing incidents, datasets, and tickets with dynamic forms and tables
- Analytics page with domain-specific metrics, charts, and visualizations (bar charts, line charts, metrics)
- Settings page for updating user role and the option to delete their account
- Session state management for authentication and user context
- Responsive UI elements: forms, tables, charts, metrics, and navigation buttons

## Technical Implementation
- UI Framework: Streamlit with multi-page support (`pages/` directory)
- Authentication: Integrated with database-backed user management and bcrypt password hashing
- Session State: Uses `st.session_state` for tracking login status, username, and role
- Navigation: `st.switch_page` for page transitions and access control
- CRUD Operations: Forms and buttons trigger database functions for incidents, datasets, and tickets
- Analytics: Uses `st.metric`, `st.bar_chart`, and `st.line_chart` for interactive visualizations
- Role Enforcement: Admin-only controls for create, update, and delete actions; warnings for unauthorized actions

## Data Disclaimer
- Disclaimer: The `Analytics` page displays synthetic (fake) data generated solely for testing and demonstration purposes. The data and any charts, metrics, or insights shown do not represent real incidents, real users, or real-world events and should not be used for operational decision-making.
- Purpose: Test UI/UX, validate visualizations, and demonstrate features during development and assessment.
- Privacy: No actual personal or sensitive data is included in these test datasets.


