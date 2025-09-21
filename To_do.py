def task():
    tasks = []
    print("Welcome to Task Management App!")

    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    def show_tasks():
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for idx, t in enumerate(tasks, 1):
                print(f"{idx}. {t}")

    show_tasks()

    while True:
        operation = int(input("\nEnter:\n 1 to add task\n 2 to update task\n 3 to delete task\n 4 to view tasks\n 5 to exit\nChoice: "))

        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' has been added successfully.")

        elif operation == 2:
            update_val = input("Enter the task you want to update: ")
            if update_val in tasks:
                up = input("Enter the new task: ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print(f"Task updated to '{up}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            delete = input("Enter the task you want to delete: ")
            if delete in tasks:
                tasks.remove(delete)
                print(f"Task '{delete}' has been deleted successfully.")
            else:
                print("Task not found.")

        elif operation == 4:
            show_tasks()

        elif operation == 5:
            print("Exiting the Task Management App. Goodbye!")
            break

        else:
            print("Invalid operation. Please try again.")

task()
