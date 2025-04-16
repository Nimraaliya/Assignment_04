import time

def countdown_liftoff():
    # Print a message before starting the countdown
    print("🚀 Countdown for spaceship launch is about to begin... Get ready!")
    time.sleep(2)  # Wait for 2 seconds before starting the countdown

    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i, end=" ")  # Print each number followed by a space
        time.sleep(1)  # Wait for 1 second between each number for a realistic countdown
    print("\nLiftoff! 🚀")  # After the countdown, print Liftoff!

def main():
    # Ask the user if they are ready to launch
    input("Press Enter to start the countdown... 🚀")
    
    # Call the countdown_liftoff function
    countdown_liftoff()

if __name__ == "__main__":
    main()
