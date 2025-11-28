# Terminal To-Do Manager
# Day 2 Mini Project

tasks = []

def show_menu():
    print("\n===== TO-DO MANAGER =====")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    task = input("Enter the task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed!")
    else:
        print("Task not found.")

def view_tasks():
    print("\nYour tasks:")
    if not tasks:
        print("No tasks added yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        remove_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")

