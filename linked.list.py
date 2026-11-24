
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = None

while True:
    print("\n1. Add  2. Remove  3. Display  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        new_node = Node(input("Enter a letter: ").upper())
        if head is None:
            head = new_node
        else:
            current = head
            while current.next is not None:
                current = current.next
            current.next = new_node
    elif choice == "2":
        if head is None:
            print("List is empty")
        else:
            print("Removed:", head.data)
            head = head.next            
    elif choice == "3":
        current = head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    elif choice == "4":
        break
    else:
        print("Invalid choice")