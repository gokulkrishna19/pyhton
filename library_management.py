# library_management.py
# Demonstrates Polymorphism in a Library Management System

class LibraryAction:
    def perform_action(self):
        raise NotImplementedError("Subclass must implement this method")


class IssueBook(LibraryAction):
    def perform_action(self):
        book = input("📖 Enter the book name to issue: ")
        student = input("Enter student name: ")
        print(f"✅ Book '{book}' issued to {student}.\n")
        return f"Issued Book → '{book}' to {student}"


class ReturnBook(LibraryAction):
    def perform_action(self):
        book = input("📚 Enter the book name to return: ")
        student = input("Enter student name: ")
        print(f"📦 Book '{book}' returned by {student}.\n")
        return f"Returned Book → '{book}' from {student}"


class ReserveBook(LibraryAction):
    def perform_action(self):
        book = input("📕 Enter the book name to reserve: ")
        student = input("Enter student name: ")
        print(f"📝 Book '{book}' reserved by {student}.\n")
        return f"Reserved Book → '{book}' for {student}"


# Polymorphic function
def perform(library_action):
    return library_action.perform_action()


# -------- Main Program --------
if __name__ == "__main__":
    print("===== 📚 Library Management System =====")

    actions = []
    while True:
        print("\n1. Issue Book")
        print("2. Return Book")
        print("3. Reserve Book")
        print("4. View All Actions")
        print("5. Exit")

        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            actions.append(perform(IssueBook()))
        elif choice == "2":
            actions.append(perform(ReturnBook()))
        elif choice == "3":
            actions.append(perform(ReserveBook()))
        elif choice == "4":
            print("\n🧾 Action History:")
            if not actions:
                print("No actions recorded yet.")
            else:
                for i, a in enumerate(actions, 1):
                    print(f"{i}. {a}")
        elif choice == "5":
            print("\n👋 Exiting Library Management System. Have a good day!")
            break
        else:
            print("⚠️ Invalid choice, please try again.")
