def double(num):
    # Multiply the given number by 2 and return the result
    return num * 2

def main():
    # Ask the user to input a number
    number = int(input("Enter a number: "))
    
    # Call the double function and print the result
    result = double(number)
    print(f"Double that is {result}")

if __name__ == "__main__":
    main()
