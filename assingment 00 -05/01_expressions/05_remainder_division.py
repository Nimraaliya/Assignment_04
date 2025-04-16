def main():
    numerator = int(input("Enter the numerator (dividend): "))
    denominator = int(input("Enter the denominator (divisor): "))

    if denominator == 0:
        print("Division by zero is not allowed.")
    else:
        remainder = numerator % denominator
        print(f"The remainder when {numerator} is divided by {denominator} is {remainder}")

if __name__ == "__main__":
    main()
