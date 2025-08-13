# A function is bock of code seperated from the atmosphare
# There are two types of functions
# 1. Pre-defined
# 2. user defined
# - to increase re-usability of code
# - a function is use less until it is not called
# syntax :
#   'def' keyword
#   def function_name(parameters):
#         body of a function

# def add(v1,v2):
#     print(f'printing {v1+v2}.....')
#
#
# print("1. add")
# print("2. sub")
# choice = int(input("Enter your selection: "))
# if choice == 1:
#     a = int(input("Enter value 1: "))
#     b = int(input("Enter value 2: "))
#     add(a,b)

# Parameters are the values to pass inside a function.
# There are two types of a parameter:
# 1. Required parameters
# 2. Default or not required parameters.

# def add(v1,v2=3):
#     print(v1+v2)
#
# add(2,v2=6)

# return keyword
# def add(v1,v2=3):
#     return v1+v2
# a = len("abcdef")
# print(a)

# a = add(1)+2
# print(a)


# Task1 : create a login function that takes 3 arguments (Email, Password and data)
# where data is a list of dictionaries containing at least 20 users data
# the function return true if email and password matches in the data
# else it returns false after calling the function store return value in status var
# and check if true show all details of that user else user not found.

data = [{"Name":"Yasir",
         "Fname":"Nawaz",
         "Email":"abc@gmail.com",
         "Password":"abc123"},
        {"Name":"Yasir2",
         "Fname":"Nawaz",
         "Email":"abc2@gmail.com",
         "Password":"abc123"},
        {"Name":"Yasir3",
         "Fname":"Nawaz",
         "Email":"abc3@gmail.com",
         "Password":"abc123"},
        {"Name":"Yasir4",
         "Fname":"Nawaz",
         "Email":"abc4@gmail.com",
         "Password":"abc123"},
        {"Name":"Yasir5",
         "Fname":"Nawaz",
         "Email":"abc5@gmail.com",
         "Password":"abc123"}]




def login(email, password, data):
    for index, user in enumerate(data):
        if user['Email'] == email and user['Password'] == password:
            return (True,index)
    else:
        return (False,-1)


email = input("Enter your email: ")
Pass = input("Enter your Pass: ")

status = login(email,Pass, data)

if status[0]:
    print("Name",data[status[1]]["Name"])
    print("FName",data[status[1]]["Fname"])
    print("Email",data[status[1]]["Email"])
else:
    print("User not found!!!")





