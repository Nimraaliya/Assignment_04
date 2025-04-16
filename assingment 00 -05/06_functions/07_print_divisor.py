def print_divisors(number):
    # Loop through all numbers from 1 to number to check for divisors
    print(f"The divisors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=" ")

def main():
    # Get input from the user
    num = int(input("Enter a number: "))
    
    # Call the function to print the divisors
    print_divisors(num)

if __name__ == "__main__":
    main()
