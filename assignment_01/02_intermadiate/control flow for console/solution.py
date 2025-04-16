import random

def play_round():
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"\nYour number is: {your_number}")
    guess = input("Is your number (H)igher or (L)ower than the computer's number? ").strip().upper()

    print(f"The computer's number was: {computer_number}")

    if (guess == "H" and your_number > computer_number) or \
       (guess == "L" and your_number < computer_number):
        print("✅ You guessed right! You earn a point.")
        return 1
    else:
        print("❌ Oops! That was incorrect.")
        return 0

def main():
    print("🎮 Welcome to the High-Low Game!")

    try:
        rounds = int(input("How many rounds do you want to play? "))
    except ValueError:
        print("Please enter a valid number.")
        return

    score = 0

    for round_num in range(1, rounds + 1):
        print(f"\n▶️ Round {round_num}")
        score += play_round()

    print(f"\n🏁 Game Over! Your final score: {score} out of {rounds}.")

if __name__ == "__main__":
    main()
