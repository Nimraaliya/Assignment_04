def get_last_element(lst):
    print(lst[-1])  # Gets the last element

def main():
    num_elements = int(input("How many elements in the list? "))
    my_list = []

    for i in range(num_elements):
        element = input(f"Enter element #{i + 1}: ")
        my_list.append(element)

    print("\nThe list you entered:", my_list)
    print("Last element:")
    get_last_element(my_list)

if __name__ == "__main__":
    main()

