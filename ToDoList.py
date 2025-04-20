import json
from Task import Task
class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.next_id = 1  # Default, will be set based on loaded tasks
        self.load_from_file()

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_to_file()
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
                self.save_to_file()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

    def mark_task_completed(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.mark_complete()
                self.save_to_file()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")

    def save_to_file(self):
        try:
            # Save tasks to the JSON file
            with open(self.filename, 'w') as file:
                json.dump([task.to_dict() for task in self.tasks], file, indent=4)
        except Exception as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
                if self.tasks:
                    self.next_id = max(task.id for task in self.tasks) + 1  # Set next_id to the highest ID + 1
        except (FileNotFoundError, json.JSONDecodeError) as e:
            # Handle errors, like if the file doesn't exist or is corrupted
            print(f"Error loading tasks from file: {e}")
            self.tasks = []
            self.next_id = 1
