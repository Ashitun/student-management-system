#auth.py
USERNAME = "Ashitun"
PASSWORD = "password123"

def login():
    """
    Authenticate the user
    Returns True if login is successful
    else returns False
    """
    user_name = input("Enter user name : ")
    password = input("Enter password : ")

    if USERNAME == user_name and PASSWORD == password :
        print("successfully logged in")
        return True
    # elif USERNAME != user_name and PASSWORD == password :
    #     print("Invalid username")
    # elif USERNAME == user_name and PASSWORD != password :
    #     print("Invalid password")
    else :
        print("Invalid User Name or Password")
        return False