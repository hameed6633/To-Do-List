from ToDoList import ToDoList

if __name__ == "__main__":
    todo = ToDoList()

    while True:
        print("\n=== TO-DO LIST MENU ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            desc = input("Enter task description (optional): ")
            todo.add_task(title, desc)

        elif choice == "2":
            todo.list_tasks()

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.mark_task_completed(task_id)
            except ValueError:
                print("Invalid input. Task ID must be a number.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Invalid input. Task ID must be a number.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
