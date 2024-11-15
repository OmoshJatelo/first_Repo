import os

# Initialize default password
default_password = "jatelo"
password_file = "password.txt"

# Function to set the initial password if the file does not exist
def initialize_password():
    if not os.path.exists(password_file):
        with open(password_file, "w") as file:
            file.write(default_password)

# Function to read the stored password
def get_stored_password():
    with open(password_file, "r") as file:
        return file.read().strip()

# Function to update the stored password
def update_password(new_password):
    with open(password_file, "w") as file:
        file.write(new_password)

# Function to attempt login
def login():
    stored_password = get_stored_password()
    attempts = 2
    for attempt in range(attempts):
        entered_password = input("Enter password: ")
        if entered_password == stored_password:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.")
    return False

# Function to reset the password
def reset_password():
    new_password = input("Enter new password: ")
    update_password(new_password)
    print("Password has been reset successfully.")

# Main program
initialize_password()  # Ensure password file is set up

if login():
    print("Access granted.")
else:
    print("Too many failed attempts.")
    reset_password()
