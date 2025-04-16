def num_in_stock(fruit):
    # Simulating Sophia's fruit store inventory using a dictionary
    inventory = {
        "apple": 50,
        "pear": 1000,
        "banana": 200,
        "orange": 300,
        "mango": 0,  # No mangoes in stock
    }

    # Check if the fruit exists in the inventory and return the stock count
    if fruit in inventory:
        return inventory[fruit]
    else:
        return 0  # Return 0 if the fruit is not in the inventory


def main():
    # Prompt user to enter a fruit
    fruit = input("Enter a fruit: ").lower()  # Convert input to lowercase for case-insensitive comparison

    # Call num_in_stock to get the number of that fruit in stock
    stock_count = num_in_stock(fruit)

    # Print the appropriate message based on the stock count
    if stock_count > 0:
        print(f"This fruit is in stock! Here is how many:\n{stock_count}")
    else:
        print("This fruit is not in stock.")


if __name__ == "__main__":
    main()
