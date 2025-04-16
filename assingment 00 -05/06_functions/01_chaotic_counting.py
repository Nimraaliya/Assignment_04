import random

def chaotic_counting(start, iterations):
    current_value = start  # Start counting from the given start value
    print(current_value, end=" ")  # Print the starting value
    
    for _ in range(iterations):
        # Randomly decide whether to add or subtract
        if random.choice([True, False]):
            change = random.randint(1, 10)  # Random increment
            current_value += change
        else:
            change = random.randint(1, 10)  # Random decrement
            current_value -= change
        
        # Print the new value after each change
        print(current_value, end=" ")

    print()  # Add a newline at the end

def main():
    start_value = int(input("Enter the starting value: "))
    iterations = int(input("Enter the number of iterations: "))
    
    chaotic_counting(start_value, iterations)

if __name__ == "__main__":
    main()
