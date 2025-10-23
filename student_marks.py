# student_marks.py
students = {}
n = int(input("Enter number of students: "))

for _ in range(n):
    name = input("Student name: ")
    marks = list(map(int, input("Enter 5 marks separated by space: ").split()))
    students[name] = marks

print("\nTotal & Average Marks:")
for name, marks in students.items():
    total = sum(marks)
    avg = total / len(marks)
    print(f"{name}: Total={total}, Average={avg:.2f}")

highest = max(students, key=lambda x: sum(students[x]))
print(f"\nHighest scoring student: {highest} with {sum(students[highest])} marks")
