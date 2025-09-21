my_id = {}

while True:
    print("\nID Management System")
    print("1. Add ID")
    print("2. View Single ID")
    print("3. Update ID")
    print("4. Delete ID")
    print("5. View Total IDs")
    print("6. Search IDs")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter the name : ")
        if name in my_id:
            print("ID already exists.")
        else:
            age = int(input("Enter the age : "))
            gmail = input("Enter the gmail : ")
            number = input("Enter the number : ")
            my_id[name] = {"age": age, "gmail": gmail, "number": number}
            print(f"ID for {name} added successfully.")

    elif choice == "2":
        name = input("Enter the ID name you want to view : ")
        if name in my_id:
            print(f"ID for {name}:")
            print(f" - Age: {my_id[name]['age']}")
            print(f" - Gmail: {my_id[name]['gmail']}")
            print(f" - Number: {my_id[name]['number']}")
        else:
            print(f"ID for {name} not found.")

    elif choice == "3":
        name = input("Enter the name : ")
        if name in my_id:
            age = int(input("Enter the age : "))
            gmail = input("Enter the gmail : ")
            number = input("Enter the number : ")
            my_id[name] = {"age": age, "gmail": gmail, "number": number}
            print(f"ID for {name} updated successfully.")
        else:
            print(f"ID for {name} not found.")

    elif choice == "4":
        name = input("Enter the ID name you want to delete : ")
        if name in my_id:
            del my_id[name]
            print(f"ID for {name} deleted successfully.")
        else:
            print(f"ID for {name} not found.")

    elif choice == "5":
        print(f"Total IDs: {len(my_id)}")

    elif choice == "6":
        search_name = input("Enter the name to search : ")
        found = False
        for name, details in my_id.items():
            if search_name.lower() in name.lower():
                print(f"ID for {name}:")
                print(f" - Age: {details['age']}")
                print(f" - Gmail: {details['gmail']}")
                print(f" - Number: {details['number']}")
                found = True
        if not found:
            print(f"ID for {search_name} not found.")

    elif choice == "7":
        print("Exiting ID Management System.")
        break

    else:
        print("Invalid choice. Please enter 1-7.")
