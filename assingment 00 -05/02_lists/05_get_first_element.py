def get_first_element(lst):
    print(lst[0])  # Since the list is guaranteed to be non-empty

def main():
    num_elements = int(input("How many elements in the list? "))
    my_list = []

    for i in range(num_elements):
        element = input(f"Enter element #{i + 1}: ")
        my_list.append(element)

    print("\nThe list you entered:", my_list)
    print("First element:")
    get_first_element(my_list)

if __name__ == "__main__":
    main()
