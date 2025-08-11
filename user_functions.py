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

def add(v1,v2):
    print(f'printing {v1+v2}.....')


print("1. add")
print("2. sub")
choice = int(input("Enter your selection: "))
if choice == 1:
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    add(a,b)
