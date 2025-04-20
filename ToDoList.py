from Task import Task
class ToDoList:
    def __init__(self):
        self.tasks = []
        self.next_id = 1  # Auto-increment task IDs

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        print(f"Task '{title}' added successfully.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                print(task)

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")
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
