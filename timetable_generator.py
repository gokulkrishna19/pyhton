# timetable_generator.py
# College Time Table Generator
# Author: Gokul Krishna

import random
from prettytable import PrettyTable

def generate_timetable(days, periods, subjects):
    timetable = {}

    for day in days:
        timetable[day] = random.sample(subjects * (len(periods)//len(subjects) + 1), len(periods))

    return timetable


def display_timetable(timetable, periods):
    table = PrettyTable()
    table.field_names = ["Day"] + periods

    for day, subs in timetable.items():
        table.add_row([day] + subs)

    print("\n=== College Time Table ===")
    print(table)


def main():
    print("📚 College Time Table Generator")
    print("-------------------------------")

    # Days and periods setup
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    periods = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]

    # Enter subjects
    subjects = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        subject = input(f"Enter subject {i+1}: ")
        subjects.append(subject)

    # Generate and display timetable
    timetable = generate_timetable(days, periods, subjects)
    display_timetable(timetable, periods)


if __name__ == "__main__":
    main()
