def is_odd(number):
    # Check if the number is odd
    if number % 2 != 0:
        return True
    else:
        return False

def main():
    # Get input from the user
    num = int(input("Enter a number: "))
    
    # Check if the number is odd
    if is_odd(num):
        print(f"{num} is odd!")
    else:
        print(f"{num} is not odd, it is even.")

if __name__ == "__main__":
    main()
