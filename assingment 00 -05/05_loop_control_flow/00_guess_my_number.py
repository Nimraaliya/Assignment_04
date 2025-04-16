import random

def guess_my_number():
    # Computer randomly selects a number between 0 and 99
    number_to_guess = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            # User input for their guess
            guess = int(input("Enter a guess: "))

            if guess < number_to_guess:
                print("Your guess is too low")
            elif guess > number_to_guess:
                print("Your guess is too high")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break  # End the game if the guess is correct
        except ValueError:
            print("Please enter a valid number.")

def main():
    guess_my_number()

if __name__ == "__main__":
    main()
