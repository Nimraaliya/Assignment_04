def main():
    # Create an empty list to store the numbers
    numbers = []

    # Ask the user how many numbers they want to input
    count = int(input("How many numbers do you want to enter? "))

    # Ask the user to input the numbers
    for i in range(count):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)

    # Calculate the average
    average = sum(numbers) / len(numbers)

    # Print the average
    print(f"The average of the numbers is: {average}")

if __name__ == "__main__":
    main()
