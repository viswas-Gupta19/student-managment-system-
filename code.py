students = {}


def add_student():
    roll_no = input("Enter roll number: ")

    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter student name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter mark for subject {i + 1}: "))
        marks.append(mark)

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully.")


def view_students():
    if not students:
        print("No students found.")
        return

    for roll_no, student in students.items():
        print("\nRoll No:", roll_no)
        print("Name:", student["name"])
        print("Marks:", student["marks"])


def search_student():
    roll_no = input("Enter roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    student = students[roll_no]

    print("\nRoll No:", roll_no)
    print("Name:", student["name"])
    print("Marks:", student["marks"])


def update_marks():
    roll_no = input("Enter roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    marks = []

    for i in range(3):
        mark = float(input(f"Enter new mark for subject {i + 1}: "))
        marks.append(mark)

    students[roll_no]["marks"] = marks

    print("Marks updated successfully.")


def delete_student():
    roll_no = input("Enter roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    del students[roll_no]

    print("Student deleted successfully.")


def calculate_average():
    roll_no = input("Enter roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    marks = students[roll_no]["marks"]

    total = sum(marks)
    average = total / len(marks)

    print("Average:", average)


def highest_scorer():
    if not students:
        print("No students found.")
        return

    highest_name = ""
    highest_average = float("-inf")

    for student in students.values():
        marks = student["marks"]
        average = sum(marks) / len(marks)

        if average > highest_average:
            highest_average = average
            highest_name = student["name"]

    print("Highest Scorer:", highest_name)
    print("Average:", highest_average)


def lowest_scorer():
    if not students:
        print("No students found.")
        return

    lowest_name = ""
    lowest_average = float("inf")

    for student in students.values():
        marks = student["marks"]
        average = sum(marks) / len(marks)

        if average < lowest_average:
            lowest_average = average
            lowest_name = student["name"]

    print("Lowest Scorer:", lowest_name)
    print("Average:", lowest_average)


def check_result():
    roll_no = input("Enter roll number: ")

    if roll_no not in students:
        print("Student not found.")
        return

    marks = students[roll_no]["marks"]
    average = sum(marks) / len(marks)

    if average >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


while True:

    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Calculate Average")
    print("7. Highest Scorer")
    print("8. Lowest Scorer")
    print("9. Pass/Fail")
    print("10. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_marks()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_average()

    elif choice == "7":
        highest_scorer()

    elif choice == "8":
        lowest_scorer()

    elif choice == "9":
        check_result()

    elif choice == "10":
        print("Thank you for using Student Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
