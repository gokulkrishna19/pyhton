# attendance_manager.py
# College Attendance Manager
# Author: Gokul Krishna

students = {}
attendance = {}

def add_student():
    print("\n--- Add Student ---")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    if roll in students:
        print("⚠️ Student already exists!\n")
    else:
        students[roll] = name
        attendance[roll] = {"Present": 0, "Total": 0}
        print(f"✅ Added student: {name}\n")

def mark_attendance():
    print("\n--- Mark Attendance ---")
    if not students:
        print("No students found. Add students first.\n")
        return

    for roll, name in students.items():
        status = input(f"{name} (Roll {roll}) - Present (P) / Absent (A): ").strip().upper()
        if status == "P":
            attendance[roll]["Present"] += 1
        attendance[roll]["Total"] += 1

    print("✅ Attendance updated successfully!\n")

def view_attendance():
    print("\n--- Attendance Report ---")
    if not students:
        print("No records found.\n")
        return

    for roll, name in students.items():
        att = attendance[roll]
        total = att["Total"]
        present = att["Present"]
        percentage = (present / total * 100) if total > 0 else 0
        print(f"{roll} - {name} | {present}/{total} Days | {percentage:.2f}% Attendance")
    print()

def main():
    while True:
        print("==== College Attendance Manager ====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance Report")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
