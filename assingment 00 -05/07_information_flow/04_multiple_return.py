def get_user_data():
    # Ask for the user's first name, last name, and email address
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")

    # Return the collected data as a tuple
    return first_name, last_name, email

def main():
    # Call the get_user_data function to get the user information
    user_data = get_user_data()

    # Print the received user data as a tuple
    print("Received the following user data:", user_data)

if __name__ == "__main__":
    main()
