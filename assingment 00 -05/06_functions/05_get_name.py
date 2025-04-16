def get_name():
    # Ask the user for their name and return it
    name = input("Enter your name: ")
    return name

def main():
    # Call the get_name function to get the name
    name = get_name()
    
    # Print a greeting using the name
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

