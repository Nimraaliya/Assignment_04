def subtract_seven(num):
    # Subtract 7 from the input number
    return num - 7

def main():
    # Prompt the user to enter a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function and print the result
    result = subtract_seven(num)
    print(f"The result after subtracting 7 is: {result}")

if __name__ == "__main__":
    main()
