def main():
    # Create an empty dictionary to store contacts
    phone_book = {}

    while True:
        print("\n📱 Phone Book Menu")
        print("1. Add contact")
        print("2. Look up contact")
        print("3. Show all contacts")
        print("4. Exit")

        # Get the user's choice
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Add a new contact to the phone book
            name = input("Enter name: ").strip()
            number = input("Enter phone number: ").strip()
            
            # Check if the contact already exists in the dictionary
            if name in phone_book:
                print(f"❗ {name} is already in the phone book.")
            else:
                phone_book[name] = number
                print(f"✅ {name} has been added to the phone book.")

        elif choice == "2":
            # Look up a contact by name
            name = input("Enter the name to look up: ").strip()
            if name in phone_book:
                print(f"📞 {name}'s number is {phone_book[name]}")
            else:
                print(f"❌ No contact found with the name {name}.")

        elif choice == "3":
            # Show all contacts in the phone book
            if phone_book:
                print("\n📒 All Contacts:")
                for name, number in phone_book.items():
                    print(f"{name}: {number}")
            else:
                print("📭 Phone book is empty.")

        elif choice == "4":
            # Exit the phone book program
            print("👋 Exiting phone book. Goodbye!")
            break

        else:
            # Handle invalid choices
            print("❗ Please choose a valid option (1-4).")

if __name__ == "__main__":
    main()
