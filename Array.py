arr = []

while True:
    print("\n1. Add  2. Remove  3. Display  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        letter = input("Enter a letter: ").upper()
        arr.append(letter)          # add at the end
    elif choice == "2":
        if len(arr) == 0:
            print("Array is empty")
        else:
            print("Removed:", arr.pop())   # remove the last letter
    elif choice == "3":
        print("Array:", arr)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
