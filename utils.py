
def line():
    print("=" *10)

def display_student(student):
    line()
    print(f"ID     : {student['id']}")
    print(f"Name   : {student['name']}")
    print(f"Age    : {student['age']}")
    print(f"Course : {student['course']}")
    line()