import random
import string

def generate_password(length=12):
    # Define character pools
    letters = string.ascii_letters  # a-z + A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&*()...

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure the password has at least one letter, digit, and symbol
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the result to avoid predictable order
    random.shuffle(password)

    return ''.join(password)

def main():
    try:
        length = int(input("Enter desired password length (minimum 6): "))
        if length < 6:
            print("Password length should be at least 6 characters.")
        else:
            new_password = generate_password(length)
            print("🔐 Your generated password is:", new_password)
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
