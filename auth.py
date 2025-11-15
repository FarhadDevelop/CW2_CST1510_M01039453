import bcrypt 
import os

# File used to store usernames and hashed passwords
USER_DATA_FILE = "users.txt"

def hash_password(plain_text_password):
    """
    Hash a plain text password.
    
    Args:
        plain_text_password (str): The plain text password to hash.
    
    Returns:
        str: The hashed password as a UTF-8 string.
    
    """
    password_bytes = plain_text_password.encode('utf-8')    # Convert to bytes
    salt = bcrypt.gensalt()                                 # Generate a salt
    hashed = bcrypt.hashpw(password_bytes, salt)            # Hash the password with the salt
    return hashed.decode('utf-8')                           # Convert back to string

def verify_password(plain_text_password, hashed_password):
    """
    Verify if a plain text password matches the stored hashed password.
    
    Args:
        plain_text_password (str): The plain text password to verify.
        hashed_password (str): The stored hashed password as a UTF-8 string.
    
    Returns:
        bool: True if the password matches, False otherwise.
    """
    plain_bytes = plain_text_password.encode('utf-8')      # Convert plain text password to bytes
    hash_bytes = hashed_password.encode('utf-8')           # Convert hashed password to bytes
    return bcrypt.checkpw(plain_bytes, hash_bytes)         # Verify the password

def user_exists(username):
    """
    Check if a username already exists in the user data file.
    
    Args:
        username (str): The username to check.
    
    Returns:
        bool: True if the username exists, False otherwise.
    """
    if not os.path.exists(USER_DATA_FILE):                # If file doesn't exist, no users exist
        return False
    
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 3:
                continue                                  # Skip malformed lines
            stored_username, _, _ = parts                 # Extract stored username
            if stored_username == username:               # Check if username matches
                return True
    return False

def register_user(username, password, role="user"):
    """
    Register a new user by saving their username and hashed password.
    
    Args:
        username (str): The username of the new user.
        password (str): The plain text password of the new user.
        role (str): The role of the user (default is "user").
    
    Returns:
        bool: True if registration is successful, False otherwise.
    """
    if user_exists(username):                             # Check if username already exists
        print(f"Error: Username '{username}' already exists.")
        return False
    hashed_password = hash_password(password)             # Hash the user's password
    with open(USER_DATA_FILE, 'a') as file:
        file.write(f"{username},{hashed_password},{role}\n")     # Save username and hashed password
    print(f"Success: User '{username}' registered successfully!")
    return True

def login_user(username, password):
    """
    Log in a user by verifying their username and password.

    Args:
        username (str): The username of the user.
        password (str): The plain text password of the user.

    Returns:
        bool: True if login is successful, False otherwise.
    """
    if not os.path.exists(USER_DATA_FILE):                # No user data file found
        print("Error: No users registered yet.")
        return False
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) < 3:
                continue                                  # Skip malformed lines
            
            stored_username, stored_hash, _ = parts

            if stored_username == username:               # If username matches
                if verify_password(password, stored_hash):
                    print(f"Success: Welcome, {username}!")   # Successful login
                    return True
                else:
                    print("Error: Invalid password.")         # Password incorrect
                    return False
                
    print("Error: Username not found.")                   # Username doesn't exist
    return False


def validate_username(username):
    """
    Validate the format of a username.

    Args:
        username (str): The username to validate.

    Returns:
        tuple: (bool, str) where bool indicates if the username is valid,
               and str provides an error message if invalid.
    """
    if len(username) < 3 or len(username) > 20 or not username.isalnum():      
        return False, "Username must be 3-20 alphanumeric characters."         
    return True, ""                                                            


def validate_password(password):
    """
    Validate the format of a password.

    Args:
        password (str): The password to validate.

    Returns:
        tuple: (bool, str) where bool indicates if the password is valid,
               and str provides an error message if invalid.
    """
    if len(password) < 6:                                                     
        return False, "Password must be at least 6 characters."
    return True, ""

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("  MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print("  Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)

def main():
    """Main program loop."""
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