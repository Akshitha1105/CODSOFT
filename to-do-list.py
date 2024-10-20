# Define an empty list to store tasks
tasks = []

# Function to add a task
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

# Function to view all tasks
def view_tasks():
    if tasks:
        print("YOUR TO-DO LIST:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("YOUR TO-DO LIST IS EMPTY!")

# Function to remove a task by its number
def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed!")
    else:
        print("Invalid task number!")

# Main loop to interact with the user
def todo_list_app():
    while True:
        print("\nTO-DO LIST APPLICATION")
        print("1. ADD TASK")
        print("2. VIEW TASKS")
        print("3. REMOVE TASK")
        print("4. EXIT")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task you want to add: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_number = int(input("Enter the number of the task to remove: "))
            remove_task(task_number)
        elif choice == '4':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

# Run the to-do list app
todo_list_app()
