import random

def generate_random_number(min_val, max_val):
    number = random.randint(min_val, max_val)
    print(f"🎲 Your random number between {min_val} and {max_val} is: {number}")

def main():
    print("🎉 Welcome to the Random Number Generator!")
    
    while True:
        try:
            min_val = int(input("Enter the minimum value: "))
            max_val = int(input("Enter the maximum value: "))
            
            if min_val > max_val:
                print("⚠️ Minimum value cannot be greater than maximum. Try again.")
                continue

            generate_random_number(min_val, max_val)
        except ValueError:
            print("❌ Please enter valid numbers.")
            continue

        again = input("Do you want to generate another number? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("👋 Thanks for using the random number generator!")
            break

if __name__ == "__main__":
    main()


