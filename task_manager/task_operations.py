from .task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        task = Task(title, description)
        self.tasks.append(task)
        print(f"Task '{title}' added successfully.")

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' removed successfully.")
                return
        print(f"Task '{title}' not found.")

    def list_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                status = "✓" if task.completed else "✗"
                print(f"{idx}. {task.title} [{status}] - {task.description}")
