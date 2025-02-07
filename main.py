from task_manager.task_operations import TaskManager
from task_manager.task_storage import save_tasks, load_tasks

def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks()

    while True:
        print("\nOptions: ")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            title = input("Task title: ")
            desc = input("Task description: ")
            task_manager.add_task(title, desc)
            save_tasks(task_manager.tasks)
        elif choice == "2":
            title = input("Task title to remove: ")
            task_manager.remove_task(title)
            save_tasks(task_manager.tasks)
        elif choice == "3":
            task_manager.list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
