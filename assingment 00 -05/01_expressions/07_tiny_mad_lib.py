def main():
    print("Let's play a tiny Mad Libs game!\n")

    # Ask for user input
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Create the story
    story = f"One day, a {adjective} {noun} decided to {verb} {adverb} through the park."

    # Display the result
    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
