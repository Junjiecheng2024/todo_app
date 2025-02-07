# Modularized To-Do List Application

## Overview
This project is a modularized to-do list application written in Python. It allows users to add, remove, and list tasks, with data persistence using JSON.

## Project Structure
```
todo_app/
├── main.py  # Main entry point
└── task_manager/
    ├── __init__.py  # Makes task_manager a package
    ├── task.py  # Defines the Task class
    ├── task_operations.py  # Handles task management
    ├── task_storage.py  # Handles saving and loading tasks
```

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/todo_app.git
cd todo_app
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
This project uses only built-in Python modules, so no additional dependencies are required.

### 4. Run the Application
```sh
python main.py
```

## Usage
- **Add Task**: Enter "1" and provide a title and description.
- **Remove Task**: Enter "2" and specify the task title to remove.
- **List Tasks**: Enter "3" to display all tasks.
- **Exit**: Enter "4" to quit the application.

## Data Persistence
All tasks are saved in `tasks.json`, allowing you to retain tasks between sessions.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

