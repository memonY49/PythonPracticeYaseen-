# print("Hello World")

# Data type:
    # 1. Premetive and 2.Non-Premetive (Primary and secondry)
    # Primary:
    # Int
    # Float
    # Char
    # Boolean
    # Secondry:
    # String
    # List
# Naming Rules:
    # 1. Name should never be started from a number.
    # 2. Name should not contain any spaces in b/w.
    # 3. Name should not be reserved words.
    # 4. Name can only contains some accepted symbols. (_)
# Vareable:
    # It is a container that contains some data tha can be changed or modified
    # Synatx of creating a variable:
        # nameofvariable = 3

# Operator:
#       Arithmetic operators:
#                     Add: +
#                     Sub: -
#                     Mul: *
#                     Dev: /
#                     Mod: %
#      Conditional Operator:
#                 less then: <
#                 greater then: >
#                 less then or equal to: <=
#                                      : >=
#                 equal to             : ==
#                 not equal            : !=
#     Logical  Operators:
#                 And
#                 Or
#                 Not

# How to take user input in python?
#    use input() to take input from user.
#    input() will always takes a string as an input.

# userin = int(input("Enter a number to print:"))
#
# print(userin-3)
#

# Take two variables as an input from the user and perform all operators on those variables.


# Conditional statements:
#    Syntax of if statement:
#           if condition:
#               body of if
#           else:
#               body of else
#           Nested if:
#           if condition:
#               body of outer if
#               if condition:
#                   body of inner if
#
#       indentation: are the white spaces before the line of code.

# x = 4
# y = 5
# w = 6

# if x>y:
#     if x < w:
#         print("x is greater than y and less than w")
#     else:
#         print("x is greater than y and greater than w")
# else:
#     print("X is less than y")



# if x>y:
#     print("x is greater than y!")
# elif x < y:
#     print("x is less than y!")
# elif x == y:
#     print("x is equal to y!")
# else:
#     print("x is not equal to y!")
#
#
# print(0.00000001 * 10000000)



# Create 6 variables to store (Name, FName, Cnic, Phone, Email and pass)
# than ask user to enter email and pass than match user_email and user_pass with stored email and pass
# if matched print all user details

# output:
# enter email: ______
# enter pass: _______
# Name: Yasir
# FName: Nawaz Ali
# CNIC: 413047836487
# Phone: 0300000000
# Email: abc@gmail.com

# comments:
#       single line: #
#       multi line:  """"""

# List:
#       A collection of elements with hetrogenius datatypes
# Syntax of a list:
#           mylist = [1,4,7,8,9,'a','b',4.6,6.7,True,False]
# how to use: listname[index]
# Index: a unique location started from 0 provided to every single element of a list
# Tuples: Same as a List but it is immutable (can not be changed or modified)

# my_list = [1,2,3,4]
# my_tuple = (1,2,3,4)
#
# my_list[2] = "three"
# my_tuple[3] = "three"
#
#
# print(my_list)
# print(my_tuple)

# Sets: A collection of elements with hetrogenius datatypes but it is distinct in nature
# and it is un ordered collection


# There are two types of a list, tuple and sets:
#   Single dimension:
#   Multi dimension:
#               List of Lists
# mylist = [1,4,5,7,3,7,7]
# mylits1 = [[1,3,4],
#            [3,4,6],
#            [2,5,7]]
# mylist2 = [[[1,2,3],
#             [3,5,7]],
#            [[7,8,0],
#             [1,6,9]]]


mylist = [[2,4,6],
          [7,9,0],
          [1,4,9]]

print(mylist[2][2])

