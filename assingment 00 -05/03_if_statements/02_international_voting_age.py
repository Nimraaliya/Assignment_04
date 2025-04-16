def check_voting_age(country, age):
    # Dictionary of voting ages for different countries
    voting_age = {
        "USA": 18,
        "Canada": 18,
        "India": 18,
        "Germany": 18,
        "Australia": 18,
        "Brazil": 16,
        "Saudi Arabia": 21,
        "Japan": 20,
        "United Kingdom": 18,
        "Pakistan":18

    }

    # Check if country is in the dictionary
    if country in voting_age:
        if age >= voting_age[country]:
            print(f"You are eligible to vote in {country}!")
        else:
            print(f"You are not eligible to vote in {country}. You need to be at least {voting_age[country]} years old.")
    else:
        print(f"Voting age information is not available for {country}.")

def main():
    country = input("Enter your country: ")
    try:
        age = int(input("Enter your age: "))
        check_voting_age(country, age)
    except ValueError:
        print("Please enter a valid age.")

if __name__ == "__main__":
    main()
