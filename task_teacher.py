# Teacher Task Management System

class TeacherTaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name, deadline):
        task = {"Task": task_name, "Deadline": deadline, "Status": "Pending"}
        self.tasks.append(task)
        print(f"✅ Task '{task_name}' added successfully!\n")

    def view_tasks(self):
        if not self.tasks:
            print("⚠️ No tasks available.\n")
            return
        print("\n📌 Teacher's Task List:")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['Task']} | Deadline: {task['Deadline']} | Status: {task['Status']}")
        print()

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["Status"] = "Completed"
            print(f"✅ Task '{self.tasks[task_index]['Task']}' marked as Completed!\n")
        else:
            print("⚠️ Invalid task number.\n")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"🗑️ Task '{removed_task['Task']}' deleted.\n")
        else:
            print("⚠️ Invalid task number.\n")


# -------- Main Program --------
def main():
    manager = TeacherTaskManager()

    while True:
        print("===== Teacher Task Management =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task_name = input("Enter task name: ")
            deadline = input("Enter deadline (dd-mm-yyyy): ")
            manager.add_task(task_name, deadline)
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.view_tasks()
            try:
                task_no = int(input("Enter task number to mark completed: ")) - 1
                manager.mark_completed(task_no)
            except ValueError:
                print("⚠️ Enter a valid number.\n")
        elif choice == "4":
            manager.view_tasks()
            try:
                task_no = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(task_no)
            except ValueError:
                print("⚠️ Enter a valid number.\n")
        elif choice == "5":
            print("👋 Exiting Teacher Task Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
