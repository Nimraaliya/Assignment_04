import random

# List of wholesome positive quotes or affirmations
wholesome_quotes = [
    "You are capable of achieving amazing things!",
    "Believe in yourself, you are stronger than you think.",
    "Don't be afraid to start over, it's a chance to rebuild what you want.",
    "Every step you take is a step toward achieving your dreams.",
    "You are enough just as you are.",
    "Great things take time. Be patient with yourself.",
    "Keep going, you're doing better than you think.",
    "Your effort today will pay off tomorrow.",
    "You have the power to create your own happiness.",
    "The world is better with you in it!",
    "You are deserving of all the wonderful things life has to offer.",
    "Success is built on the foundation of small, consistent actions."
]

def wholesome_machine():
    # Randomly select a quote
    quote = random.choice(wholesome_quotes)
    
    # Display the positive quote
    print(f"\n💖 Wholesome Machine says: {quote} 💖")

def main():
    print("Welcome to the Wholesome Machine! 🌟\n")
    input("Press Enter to get your wholesome quote...")  # Wait for the user to press Enter
    
    # Call the wholesome machine function
    wholesome_machine()

if __name__ == "__main__":
    main()
