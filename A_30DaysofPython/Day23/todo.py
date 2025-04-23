tasks = []

while True:
    print("\n ---- To-Do List----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print('Task Added Successfully')

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    elif choice == "3":
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")