def fibonacci_up_to_max_value(max_value):
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    fibonacci_sequence = []  # List to store the Fibonacci numbers
    
    # Generate Fibonacci numbers until we reach or exceed max_value
    while a < max_value:
        fibonacci_sequence.append(a)  # Store each Fibonacci number
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
    
    return fibonacci_sequence

def print_fibonacci_info(fibonacci_sequence):
    # Print the Fibonacci sequence
    print("Fibonacci sequence up to the given limit:")
    print(" ".join(map(str, fibonacci_sequence)))

    # Count the number of terms
    print("\nNumber of terms in the sequence:", len(fibonacci_sequence))

    # Calculate the sum of the Fibonacci numbers
    total_sum = sum(fibonacci_sequence)
    print("Sum of the Fibonacci sequence:", total_sum)

def main():
    # Ask the user for the maximum value for the Fibonacci sequence
    try:
        MAX_VALUE = int(input("Enter the maximum value for the Fibonacci sequence: "))
        if MAX_VALUE <= 0:
            print("Please enter a positive number greater than 0.")
            return

        # Get the Fibonacci sequence up to the maximum value
        fibonacci_sequence = fibonacci_up_to_max_value(MAX_VALUE)

        # Print the Fibonacci sequence and related information
        print_fibonacci_info(fibonacci_sequence)

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
