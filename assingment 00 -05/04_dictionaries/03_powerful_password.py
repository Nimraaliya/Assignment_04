import hashlib

# Hash function that simulates hashing the password
def hash_password(password):
    """Returns the SHA256 hash of the password."""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the provided email and password_to_check match the stored password hashes.
    Returns True if the password is correct, False otherwise.
    """
    # Hash the password entered by the user
    hashed_password = hash_password(password_to_check)
    
    # Check if the email exists in the stored logins and if the hashes match
    if email in stored_logins and stored_logins[email] == hashed_password:
        return True
    return False

def main():
    # Simulate a stored logins dictionary (email -> hashed password)
    stored_logins = {
        "user@example.com": hash_password("securePassword123"),
        "admin@website.com": hash_password("adminPass456"),
        "guest@platform.com": hash_password("guest1234")
    }

    # User input for login
    email = input("Enter your email: ")
    password_to_check = input("Enter your password: ")

    # Check if login is successful
    if login(email, password_to_check, stored_logins):
        print("Login successful!")
    else:
        print("Invalid email or password.")

if __name__ == "__main__":
    main()
