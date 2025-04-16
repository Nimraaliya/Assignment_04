def main():
    counts = {}

    while True:
        num = input("Enter a number (or press Enter to finish): ")
        if num == "":
            break
        
        if num.isdigit():
            num = int(num)
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        else:
            print("Please enter a valid number.")

    print("\nFrequency of each number:")
    for number, count in counts.items():
        print(f"{number} appears {count} times.")

if __name__ == "__main__":
    main()
