import random

def play_round():
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"\nYour number is: {your_number}")
    guess = input("Do you think your number is (H)igher or (L)ower than the computer's number? ").strip().upper()

    print(f"The computer's number was: {computer_number}")

    if (guess == 'H' and your_number > computer_number) or \
       (guess == 'L' and your_number < computer_number):
        print("🎉 You guessed correctly! You earn a point.")
        return 1
    else:
        print("❌ Incorrect guess. No point this round.")
        return 0

def main():
    print("🎲 Welcome to the High-Low Game!")
    rounds = int(input("How many rounds would you like to play? "))
    score = 0

    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        score += play_round()

    print(f"\n🏁 Game over! Your final score: {score} out of {rounds}")

if __name__ == "__main__":
    main()
