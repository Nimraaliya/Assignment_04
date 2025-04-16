import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02d}:{secs:02d}"
        print(time_format, end='\r')  # Print on the same line
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!")

def main():
    try:
        user_input = int(input("Enter time in seconds: "))
        print("Starting countdown...")
        countdown_timer(user_input)
    except ValueError:
        print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    main()
