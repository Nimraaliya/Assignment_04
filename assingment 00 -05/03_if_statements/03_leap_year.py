def is_leap_year(year):
    # A year is a leap year if it's divisible by 4
    # Except for years divisible by 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
