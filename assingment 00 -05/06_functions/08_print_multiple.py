def print_multiples(number, count):
    print(f"The first {count} multiples of {number} are:")
    for i in range(1, count + 1):
        print(number * i, end=" ")

def main():
    num = int(input("Enter a number: "))
    how_many = int(input("How many multiples to print? "))
    
    print_multiples(num, how_many)

if __name__ == "__main__":
    main()
