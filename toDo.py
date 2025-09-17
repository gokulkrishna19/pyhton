# todo_app.py
# Simple Command-Line To-Do List Application

def show_menu():
    print("\n==== TO-DO LIST MENU ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet! 🎉")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"✅ Task '{task}' added!")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            choice = int(input("Enter task number to remove: "))
            removed = tasks.pop(choice - 1)
            print(f"❌ Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("⚠️ Invalid choice!")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("⚠️ Invalid option, try again!")

if __name__ == "__main__":
    main()