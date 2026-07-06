from database import load_students , save_students
from utils import line , display_student

def add_student():

    """
    Add a new student to the json
    """
    name = input("Enter the name : ")
    
    while True :
        try:
            age = int(input("Enter age : "))
            break
        except ValueError:
            print("Age must be an number")

    course = input("Enter course : ")
    students = load_students()
    student = {
            "id": len(students) + 1,
            "name" : name,
            "age" : age,
            "course" : course
            }
        
    students.append(student)
    save_students(students)

    print("\nStudent Added Successfully!\n")

def view_students():
    """Display all students"""

    students = load_students()

    if len(students) == 0 :
        print("\n No students found!\n")
        return
    line()

    print("STUDENTS LIST")

    line()

    for student in students :
        display_student(student)

def search_student():

    students = load_students()

    if len(students) == 0:
        print("\nNo Students Found!\n")
        return

    search_name = input("Enter Student Name : ")

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            print("\nStudent Found\n")

            display_student(student)

            found = True
            break

    if not found:
        print("\nStudent Not Found\n")

def update_student():
    students = load_students()
    if len(students) == 0 :
        print("\nNo students found")

    try:
        student_id = int(input("Enter student id : "))
    except ValueError :
        print("Invalid ID ")
        return 
    
    found = False 

    for student in students :
        if student["id"] == student_id :
            print("\nCurrent Student Details")
            display_student(student)

            student["name"] = input("Enter new name : ")
            while True:
                try:
                    student["age"] = int(input("Enter New Age : "))
                    break
                except ValueError:
                    print("Age must be a number.")

            student["course"] = input("Enter New Course : ")

            save_students(students)

            print("\nStudent Updated Successfully!")

            found = True
            break

    if not found:
        print("Student Not Found.")

def delete_student():

    students = load_students()

    if len(students) == 0:
        print("\nNo students found.\n")
        return

    try:
        student_id = int(input("Enter Student ID to delete: "))
    except ValueError:
        print("Invalid ID")
        return

    found = False

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found")

            display_student(student)

            confirm = input("Are you sure? (Y/N): ")

            if confirm.lower() == "y":
                students.remove(student)
                save_students(students)
                print("\nStudent Deleted Successfully!\n")
            else:
                print("\nDeletion Cancelled.\n")

            found = True
            break

    if not found:
        print("\nStudent Not Found.\n")



