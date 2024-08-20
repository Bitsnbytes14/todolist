import os

# Function to load tasks from the file
def load_tasks(filename='tasks.txt'):
    if not os.path.exists(filename):
        return []
    with open(filename, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

# Function to save tasks to the file
def save_tasks(tasks, filename='tasks.txt'):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# Function to display all tasks
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
        return
    print("Your To-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Added: {task}")

# Function to remove a task
def remove_task(tasks):
    display_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"Removed: {removed_task}")
    except (ValueError, IndexError):
        print("Invalid task number.")

# Function to show the menu
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Main function
def main():
    print("Starting To-Do List Application...")
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
