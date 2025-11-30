todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour To-Do Tasks:")
        if not todo_list:
            print("No tasks found.")
        else:
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not todo_list:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(todo_list):
                removed = todo_list.pop(num-1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Try again.")
# TO-do-list
