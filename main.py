from task_manager.task_operations import TaskManager
from task_manager.task_storage import save_tasks, load_tasks

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks()

    while True:
        print("\nOptions: ")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            if not task_manager.tasks:
                print("\nNo tasks available.")
            else:
                print("\nTo-Do List:")
                for idx, task in enumerate(task_manager.list_tasks(), start=1):
                    status = "✓" if task.completed else "✗"
                    print(f"{idx}. {task.title} [{status}] - {task.description}")
        elif choice == "2":
            title = input("Task title: ")
            desc = input("Task description: ")
            task_manager.add_task(title, desc)
            save_tasks(task_manager.tasks)
        elif choice == "3":
            title = input("Task title to remove: ")
            task_manager.remove_task(title)
            save_tasks(task_manager.tasks)
        elif choice == "4":
            title = input("Task title to mark as completed: ")
            for task in task_manager.tasks:
                if task.title == title:
                    task.mark_completed()
            save_tasks(task_manager.tasks)
        elif choice == "5":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
