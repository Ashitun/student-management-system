import json

FILENAME = "students.json"

def load_students() :
    """
    Load students from the JSON file.
    Returns a list of students.
    """
    try:
        with open(FILENAME,"r") as file :
            students = json.load(file)
            return students
    except FileNotFoundError :
        return []
    
def save_students(students) :
    """
    Save students to the JSON file.
    """
    with open(FILENAME,"w") as file :
        json.dump(students,file,indent = 4)

# def view_students():
#     with open(FILENAME,"r") as file :
#         json.load(file)
