def main():
    # Dictionary of fruit prices
    fruit_prices = {
        'apple': 2.5,
        'banana': 10.0,
        'strawberry': 7.0,
        'kiwi': 3.0,
        'cherry': 5.5,
        'mango': 4.0,
        'orange': 2.3
    }

    total_cost = 0

    # Loop through the dictionary and ask the user how many of each fruit they want to buy
    for fruit, price in fruit_prices.items():
        # Ask the user for the quantity of each fruit
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += price * quantity  # Calculate the cost for this fruit and add to total

    # Print the total cost
    print(f"\nYour total is ${total_cost:.2f}")

if __name__ == "__main__":
    main()
