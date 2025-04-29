# # Manages a list of tasks
# tasks = []

# while True:
#     print("\n1. Add Task\n2. View Tasks\n3. Exit")
#     choice = input("Enter choice: ")
#     if choice == '1':
#         task = input("Enter task: ")
#         tasks.append(task)
#     elif choice == '2':
#         for i, task in enumerate(tasks, 1):
#             print(f"{i}. {task}")
#     elif choice == '3':
#         break
#     else:
#         print("Invalid choice")
# if delete function be implement karna bola 
# Manages a list of tasks with Add, View, Delete, and Exit options
tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Delete Task\n4. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)  # Adds task to the list

    elif choice == '2':
        if not tasks:
            print("No tasks to show.")
        else:
            print("Task List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")  # Displays task number and task

    elif choice == '3':
        if not tasks:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)  # Removes task by index
                    print(f"Task '{removed}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == '4':
        print("Exiting Task Manager.")
        break

    else:
        print("Invalid choice. Please enter 1-4.")
