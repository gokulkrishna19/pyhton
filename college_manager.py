# college_manager.py
# Simple College Management System (Console Based)
# Author: Gokul Krishna

students = []

def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    year = input("Enter Year: ")

    student = {
        "roll": roll,
        "name": name,
        "course": course,
        "year": year
    }
    students.append(student)
    print(f"✅ Student '{name}' added successfully!\n")


def view_students():
    print("\n--- Student List ---")
    if not students:
        print("No records found.\n")
        return

    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Course: {s['course']}, Year: {s['year']}")
    print()


def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter Roll Number to search: ")
    for s in students:
        if s['roll'] == roll:
            print(f"Found: {s}")
            return
    print("❌ Student not found.\n")


def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter Roll Number to update: ")
    for s in students:
        if s['roll'] == roll:
            s['name'] = input("Enter new Name: ")
            s['course'] = input("Enter new Course: ")
            s['year'] = input("Enter new Year: ")
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found.\n")


def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter Roll Number to delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("🗑️ Student deleted successfully!\n")
            return
    print("❌ Student not found.\n")


def main():
    while True:
        print("==== College Manager ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
