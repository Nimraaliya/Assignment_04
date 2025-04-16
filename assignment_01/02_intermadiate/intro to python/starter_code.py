# Starter Code Example in Python

# Define a function that does something useful
def example_function(parameter):
    # Placeholder for some processing logic
    return parameter * 2  # Simple operation for demonstration

# Main function where the program begins
def main():
    # Ask the user for input
    user_input = input("Please enter a number: ")

    try:
        # Convert input to a number (assuming user inputs a valid number)
        number = float(user_input)
        
        # Call the example function with the input
        result = example_function(number)

        # Display the result
        print(f"The result is: {result}")
    
    except ValueError:
        # Handle invalid input (non-numeric input)
        print("Please enter a valid number.")

# If this script is run directly (not imported), execute the main function
if __name__ == "__main__":
    main()
