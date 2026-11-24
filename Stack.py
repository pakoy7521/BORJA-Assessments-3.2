stack = []

while True:
    print("\n1. Push  2. Pop  3. Display  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        letter = input("Enter a letter: ").upper()
        stack.append(letter)            # push on top
    elif choice == "2":
        if len(stack) == 0:
            print("Stack is empty")
        else:
            print("Popped:", stack.pop())   # remove from top
    elif choice == "3":
        print("Stack (bottom to top):", stack)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
