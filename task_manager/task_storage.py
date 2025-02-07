import json
from .task import Task

TASK_FILE = "tasks.json"

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

def load_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            task_dicts = json.load(f)
            return [Task(**task) for task in task_dicts]
    except FileNotFoundError:
        print("No task file found. Starting with an empty task list.")
    except json.JSONDecodeError:
        print("Error: Task file is corrupted. Starting with an empty task list.")
    return []
