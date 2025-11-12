import bcrypt 
import os

# File used to store usernames and hashed passwords
USER_DATA_FILE = "users.txt"

# Function to hash a plain text password using bcrypt
def hash_password(plain_text_password):
    password_bytes = plain_text_password.encode('utf-8')   # Convert plain text to bytes
    salt = bcrypt.gensalt()                               # Generate a unique salt
    hashed = bcrypt.hashpw(password_bytes, salt)          # Hash password with salt
    return hashed.decode('utf-8')                         # Return hashed password as a string

# Function to verify if a plain text password matches the stored hash
def verify_password(plain_text_password, hashed_password):
    plain_bytes = plain_text_password.encode('utf-8')     # Convert input password to bytes
    hash_bytes = hashed_password.encode('utf-8')          # Convert stored hash to bytes
    return bcrypt.checkpw(plain_bytes, hash_bytes)        # Compare password and hash

# Function to check if a username already exists in the file
def user_exists(username):
    if not os.path.exists(USER_DATA_FILE):                # If file doesn't exist, no users exist
        return False
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            stored_username, _ = line.strip().split(',')  # Split username and password
            if stored_username == username:               # Check if username matches
                return True
    return False

# Function to register a new user
def register_user(username, password, role="user"):
    if user_exists(username):                             # Check if username already exists
        print(f"Error: Username '{username}' already exists.")
        return False
    hashed_password = hash_password(password)             # Hash the user's password
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{hashed_password},{role}\n")     # Save username and hashed password
    print(f"Success: User '{username}' registered successfully!")
    return True

# Function to log in a user
def login_user(username, password, role="user"):
    if not os.path.exists(USER_DATA_FILE):                # No user data file found
        print("Error: No users registered yet.")
        return False
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            stored_username, stored_hash, stored_role = line.strip().split(',')
            if stored_username == username:               # If username matches
                if verify_password(password, stored_hash):
                    print(f"Success: Welcome, {username}!")   # Successful login
                    return True
                else:
                    print("Error: Invalid password.")         # Password incorrect
                    return False
    print("Error: Username not found.")                   # Username doesn't exist
    return False

# Function to validate username format
def validate_username(username):
    if len(username) < 3 or len(username) > 20 or not username.isalnum():
        return False, "Username must be 3-20 alphanumeric characters."
    return True, ""

# Function to validate password format
def validate_password(password):
    if len(password) < 6:
        return False, "Password must be at least 6 characters."
    return True, ""

# Function to display the main menu
def display_menu():
    print("\n" + "="*50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

# Main function to run the program
def main():
    print("\nWelcome to the Week 7 Authentication System!")
    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':  # Registration option
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()
            is_valid, error = validate_username(username)
            if not is_valid:
                print(f"Error: {error}")
                continue
            password = input("Enter a password: ").strip()
            is_valid, error = validate_password(password)
            if not is_valid:
                print(f"Error: {error}")
                continue
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue
            register_user(username, password, role="user")

        elif choice == '2':  # Login option
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            login_user(username, password)
            input("\nPress Enter to return to main menu...")

        elif choice == '3':  # Exit program
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break

        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")

# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()