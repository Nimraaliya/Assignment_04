import random

NUM_SIDES = 6

# Function to roll two dice
def roll_dice():
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print(f"Die 1: {die1}, Die 2: {die2}, Total: {total}")

# Main function
def main():
    die1 = 10  # Just to test variable scope
    print(f"die1 in main() starts as {die1}")

    for _ in range(3):
        roll_dice()
        print(f"die1 in main() is still {die1}")

# Entry point
if __name__ == "__main__":
    main()

      