def count_even_in_list(numbers):
    count = 0  # Initialize a counter for even numbers
    
    # Loop through the list and check for even numbers
    for number in numbers:
        if number % 2 == 0:
            count += 1  # Increment the counter if the number is even
            
    print(f"There are {count} even numbers in the list.")

def main():
    # Example list of numbers
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    
    count_even_in_list(numbers)

if __name__ == "__main__":
    main()
