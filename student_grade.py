student_grades = {}

# Add student details
def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added student {name} with grade {grade}.")

# update student info
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} and {grade} updated successfully.")
    else:
        print(f"Student {name} not found.")

# delete student info 
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"Deleted student {name}.")
    else:
        print(f"Student {name} not found.")

# view all students
def view_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"Student: {name}, Grade: {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("Welcome to the Student Grade Management System")
        print("1. Add Student")
        print("2. update Student")
        print("3. delete Student")
        print("4. view Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name, grade)
        elif choice == '2':
            name = input("Enter student name to update: ")
            grade = input("Enter new grade: ")
            update_student(name, grade)
        elif choice == '3':
            name = input("Enter student name to delete: ")
            delete_student(name)
        elif choice == '4':
            view_students()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


main()