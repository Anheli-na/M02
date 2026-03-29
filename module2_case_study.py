# Name: Anhelina Hodunko
# File Name: module2_case_study.py
# Description: This program accepts student names and GPAs
# and determines whether a student qualifies for the Dean's List or Honor Roll.

while True:
    last_name = input("Enter the student's last name (or ZZZ to quit): ")

    if last_name == "ZZZ":
        break

    first_name = input("Enter the student's first name: ")
    gpa = float(input("Enter the student's GPA: "))

    print(f"\nStudent: {first_name} {last_name}")

    if gpa >= 3.5:
        print("The student has made the Dean's List.")
    elif gpa >= 3.25:
        print("The student has made the Honor Roll.")
    else:
        print("The student did not qualify for either list.")

    print()