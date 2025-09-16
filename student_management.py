# student_management.py
# A simple student management system (approx 30 lines)

students = []

def add_student(name, roll, marks):
    students.append({"name": name, "roll": roll, "marks": marks})

def view_students():
    if not students:
        print("No students found!")
    else:
        for s in students:
            print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")

def search_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None

if __name__ == "__main__":
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            roll = input("Enter roll number: ")
            marks = int(input("Enter marks: "))
            add_student(name, roll, marks)
            print("✅ Student added!")
        elif choice == "2":
            view_students()
        elif choice == "3":
            roll = input("Enter roll number to search: ")
            student = search_student(roll)
            if student:
                print(f"Found -> Roll: {student['roll']}, Name: {student['name']}, Marks: {student['marks']}")
            else:
                print("❌ Student not found!")
        elif choice == "0":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice! Try again.")
