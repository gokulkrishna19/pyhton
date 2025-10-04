# teacher_task_manager.py
# Demonstrates Polymorphism in a Teacher Task Management System

class Task:
    def assign_task(self):
        raise NotImplementedError("Subclass must implement this method")


class ClassTask(Task):
    def assign_task(self):
        subject = input("📘 Enter subject name: ")
        topic = input("Enter topic to teach: ")
        print(f"✅ Class task assigned: Teach '{topic}' in {subject}.\n")
        return f"Class Task → Subject: {subject}, Topic: {topic}"


class ExamTask(Task):
    def assign_task(self):
        exam_name = input("📝 Enter exam name: ")
        date = input("Enter exam date (DD/MM): ")
        print(f"✅ Exam task assigned: {exam_name} on {date}.\n")
        return f"Exam Task → {exam_name}, Date: {date}"


class ProjectTask(Task):
    def assign_task(self):
        project_title = input("💻 Enter project title: ")
        team_size = int(input("Enter team size: "))
        print(f"✅ Project '{project_title}' assigned to team of {team_size} students.\n")
        return f"Project Task → Title: {project_title}, Team Size: {team_size}"


# Polymorphic function
def assign(task_type):
    return task_type.assign_task()


# -------- Main Program --------
if __name__ == "__main__":
    print("===== 🎓 Teacher Task Management System =====")

    tasks = []
    while True:
        print("\n1. Assign Class Task")
        print("2. Assign Exam Task")
        print("3. Assign Project Task")
        print("4. View All Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            tasks.append(assign(ClassTask()))
        elif choice == "2":
            tasks.append(assign(ExamTask()))
        elif choice == "3":
            tasks.append(assign(ProjectTask()))
        elif choice == "4":
            print("\n🧾 Assigned Tasks:")
            if not tasks:
                print("No tasks assigned yet.")
            else:
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")
        elif choice == "5":
            print("\n👋 Exiting Teacher Task Manager.")
            break
        else:
            print("⚠️ Invalid choice, try again.")
