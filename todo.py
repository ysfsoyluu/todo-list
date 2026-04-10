# To-Do List App
# Author: Yusuf Soylu
# A beginner Python project — manage your daily tasks from the terminal

tasks = []


def view_tasks():
    print("\n--- Your Tasks ---")
    if len(tasks) == 0:
        print("No tasks yet. Add one!")
    else:
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "⬜"
            print(f"  {index}. {status} {task['name']}")
    print("------------------")


def add_task():
    name = input("Enter task name: ")
    if name.strip() == "":
        print("Task name cannot be empty.")
        return
    tasks.append({"name": name, "done": False})
    print(f"Task '{name}' added!")


def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to mark as complete: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print(f"Task '{tasks[number - 1]['name']}' marked as complete! ✅")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Task '{removed['name']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def todo_app():
    print("==============================")
    print("      To-Do List App 📝       ")
    print("==============================")

    while True:
        print("\nWhat would you like to do?")
        print("  1 — View all tasks")
        print("  2 — Add a task")
        print("  3 — Complete a task ✅")
        print("  4 — Delete a task")
        print("  5 — Quit")
        print("------------------------------")

        choice = input("Choose an option (1/2/3/4/5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("See you later! 👋")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


todo_app()
