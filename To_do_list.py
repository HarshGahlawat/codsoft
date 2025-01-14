import json
import os
class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False
    def mark_complete(self):
        self.completed = True
    def mark_incomplete(self):
        self.completed = False
    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"[{status}] {self.title}: {self.description}"
TASKS_FILE = "tasks.json"
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            tasks_data = json.load(file)
            return [Task(**task) for task in tasks_data]
    return []
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump([task.__dict__ for task in tasks], file)
def add_task(tasks, title, description=""):
    tasks.append(Task(title, description))
def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")
def update_task(tasks, index, title, description):
    tasks[index].title = title
    tasks[index].description = description
def delete_task(tasks, index):
    tasks.pop(index)
def mark_task_complete(tasks, index):
    tasks[index].mark_complete()
def mark_task_incomplete(tasks, index):
    tasks[index].mark_incomplete()
def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Mark Task as Incomplete")
        print("7. Save and Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title: ")
            description = input("Enter new description: ")
            update_task(tasks, index, title, description)
        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == "5":
            index = int(input("Enter task number to mark as complete: ")) - 1
            mark_task_complete(tasks, index)
        elif choice == "6":
            index = int(input("Enter task number to mark as incomplete: ")) - 1
            mark_task_incomplete(tasks, index)
        elif choice == "7":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
