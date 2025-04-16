def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))  # Convert the input to an integer

    # Loop until curr_value is 100 or greater
    while curr_value < 100:
        # Double the current value
        curr_value *= 2
        
        # Print the doubled value
        print(curr_value, end=" ")  # Print the result on the same line with spaces between values

if __name__ == "__main__":
    main()
