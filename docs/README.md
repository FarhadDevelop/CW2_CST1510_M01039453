# CW2 for module CST1510
Final project for module CST1510 involving developing a substantial Streamlit application incorporating Data Science, Cyber Security, and IT

# Week 7: Secure Authentication System
- Student Name: Farhad Binu Manaf
- Student ID: M01039453
- Course: CST1510 - Multi-Domain Intelligence Platform

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