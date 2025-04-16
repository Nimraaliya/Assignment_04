def check_height(height):
    min_height = 120  # Minimum height in cm to ride
    if height >= min_height:
        print("You're tall enough to ride! 🎉")
    else:
        print(f"Sorry, you need to be at least {min_height} cm to ride.")

def main():
    try:
        height = int(input("Enter your height in cm: "))
        check_height(height)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
