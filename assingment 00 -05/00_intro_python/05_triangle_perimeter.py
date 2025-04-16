def main():
    try:
        # Taking input from the user
        side1 = float(input("Enter the length of side 1: "))
        side2 = float(input("Enter the length of side 2: "))
        side3 = float(input("Enter the length of side 3: "))

        # Calculating perimeter
        perimeter = side1 + side2 + side3

        # Displaying result
        print(f"The perimeter of the triangle is {perimeter}")
    
    except ValueError:
        print("Please enter valid numeric values for the sides.")

if __name__ == "__main__":
    main()
