import os
import pickle

# Define the task class
class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

# Load tasks from file
def load_tasks():
    if os.path.exists('tasks.pkl'):
        with open('tasks.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.pkl', 'wb') as f:
        pickle.dump(tasks, f)

# Display the to-do list
def display_tasks(tasks):
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {'[X]' if task.completed else '[ ]'} {task.name}")

# Add a new task
def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks.append(Task(task_name))
    print("Task added successfully.")

# Mark a task as done or undone
def toggle_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to toggle: "))
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1].completed = not tasks[task_index - 1].completed
        print("Task status updated.")
    else:
        print("Invalid task number.")

# Remove a task
def remove_task(tasks):
    display_tasks(tasks)
    task_index = int(input("Enter the task number to remove: "))
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task.name}")
    else:
        print("Invalid task number.")

# Main program loop
def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Toggle Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            toggle_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
