def main():
    my_list = []

    while True:
        value = input("Enter a value: ")
        
        if value == "":  # If the input is empty, break out of the loop
            break
        
        my_list.append(value)  # Add the value to the list
        
    print("Here's the list:", my_list)

if __name__ == "__main__":
    main()
