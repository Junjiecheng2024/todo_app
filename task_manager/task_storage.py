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
    except (FileNotFoundError, json.JSONDecodeError):
        return []
