def print_ones_digit(num):
    # Get the absolute value to handle negatives, then get the ones digit
    ones = abs(num) % 10
    print(f"The ones digit is {ones}")

def main():
    number = int(input("Enter a number: "))
    print_ones_digit(number)

if __name__ == "__main__":
    main()
