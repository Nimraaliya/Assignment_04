
def add_three_copies(some_list, data):
    for _ in range(3):
        some_list.append(data)

def main():
    message = input("Enter a message to copy: ")

    my_list = []
    print("\nList before:", my_list)

    add_three_copies(my_list, message)

    print("List after:", my_list)

if __name__ == "__main__":
    main()
