import re


def is_valid_student_name(name):
    """Check if the student name is valid (no special characters or numbers)."""
    return bool(re.match(r'^[a-zA-Z\s]+$', name))


def is_valid_grade(grade):
    """Check if the grade is a valid number."""
    try:
        float(grade)
        return True
    except ValueError:
        return False


def add_student(grades, name):
    """Add a new student to the grades list with an empty grade list."""
    if not is_valid_student_name(name):
        print("Error: Invalid student name. Only alphabets and spaces are allowed.")
        return
    grades.append([name, []])
    print(f"Student '{name}' added successfully.")


def add_grade(grades, name, grade):
    """Add a grade to the grade list of the specified student."""
    if not is_valid_student_name(name):
        print("Error: Invalid student name. Only alphabets and spaces are allowed.")
        return
    if not is_valid_grade(grade):
        print("Error: Invalid grade. Please enter a valid number.")
        return
    grade = float(grade)
    for student in grades:
        if student[0] == name:
            student[1].append(grade)
            print(f"Grade {grade} added for student '{name}'.")
            return

    print(f"Error: Student '{name}' not found.")


def calculate_average(grades, name):
    """Calculate the average grade of the specified student."""
    if not is_valid_student_name(name):
        print("Error: Invalid student name. Only alphabets and spaces are allowed.")
        return
    for student in grades:
        if student[0] == name:
            grades_list = student[1]
            if len(grades_list) > 0:
                return sum(grades_list) / len(grades_list)
            else:
                return 0.0
    print(f"Error: Student '{name}' not found.")


def calculate_class_average(grades):
    """Calculate the average grade for the entire class."""
    total_grades = []
    for student in grades:
        total_grades.extend(student[1])
    if len(total_grades) > 0:
        return sum(total_grades) / len(total_grades)
    else:
        return 0.0


def display_student_grades(grades, name):
    """Display the grades of the specified student."""
    if not is_valid_student_name(name):
        print("Error: Invalid student name. Only alphabets and spaces are allowed.")
        return
    for student in grades:
        if student[0] == name:
            grades_list = student[1]
            if len(grades_list) > 0:
                print(f"Grades of {name}: {', '.join(map(str, grades_list))}") #To convert the string into float
            else:
                print(f"No grades found for {name}.")
            return
    print(f"Error: Student '{name}' not found.")


def display_menu():
    """Display the menu options."""
    print("---------------------------------------------")
    print("\n\t  STUDENT GRADE ANALYZER:")
    print("---------------------------------------------")
    print("1. Add student")
    print("2. Add grade")
    print("3. Calculate average grade for a student")
    print("4. Calculate class average grade")
    print("5. Display student grades")
    print("6. Exit")
    print("---------------------------------------------")


def main():
    grades = []  # Intialize a grades with empty list
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("***ADDING A STUDENT***")
            name = input("Enter student name: ")
            add_student(grades, name)

        elif choice == '2':
            print("***ADDING GRADE***")
            name = input("Enter student name: ")
            grade = input("Enter grade: ")
            add_grade(grades, name, grade)

        elif choice == '3':
            print("***CALCULATE AVERAGE GRADE FOR A STUDENT***")
            name = input("Enter student name: ")
            average = calculate_average(grades, name)
            if average is not None:
                print(f"Average grade of {name}: {average}")

        elif choice == '4':
            print("***CALCULATING A CLASS AVERAGE***")
            class_average = calculate_class_average(grades)
            print(f"Class average grade: {class_average}")

        elif choice == '5':
            print("***DISPLAY STUDENTS GRADES***")
            name = input("Enter student name: ")
            display_student_grades(grades, name)

        elif choice == '6':
            print("...Exiting the program and thank you for using ...:)")

            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
