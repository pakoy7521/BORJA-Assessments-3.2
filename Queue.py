queue = []

while True:
    print("\n1. Enqueue  2. Dequeue  3. Display  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        letter = input("Enter a letter: ").upper()
        queue.append(letter)            # add at the rear
    elif choice == "2":
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Dequeued:", queue.pop(0))
    elif choice == "3":
        print("Queue (front to rear):", queue)
    elif choice == "4":
        break
    else:
        print("Invalid choice")