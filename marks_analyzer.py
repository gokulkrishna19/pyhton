# marks_analyzer.py
# Student Marks Analyzer
# Author: Gokul Krishna

students = {}

def add_student():
    print("\n--- Add Student Marks ---")
    name = input("Enter Student Name: ")
    num_subjects = int(input("Enter number of subjects: "))

    marks = []
    for i in range(num_subjects):
        mark = float(input(f"Enter mark for Subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / num_subjects

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B+"
    elif average >= 60:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    students[name] = {
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    print(f"✅ Marks added for {name}!\n")

def view_results():
    print("\n--- Student Results ---")
    if not students:
        print("No records found.\n")
        return

    for name, info in students.items():
        print(f"Name: {name}")
        print(f"Marks: {info['marks']}")
        print(f"Total: {info['total']}")
        print(f"Average: {info['average']:.2f}")
        print(f"Grade: {info['grade']}")
        print("-" * 30)

def topper():
    if not students:
        print("\nNo data available.\n")
        return

    top_student = max(students.items(), key=lambda x: x[1]["average"])
    name, info = top_student
    print(f"\n🏆 Topper: {name} with {info['average']:.2f}% ({info['grade']})\n")

def main():
    while True:
        print("==== Student Marks Analyzer ====")
        print("1. Add Student Marks")
        print("2. View Results")
        print("3. Show Topper")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_results()
        elif choice == "3":
            topper()
        elif choice == "4":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Try again.\n")

if __name__ == "__main__":
    main()
