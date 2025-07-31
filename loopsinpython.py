# Loops in python:
#  There are two types of loops available in python.
#       1.For loop
#       2.While loop
# For Loop:
#   Syntax:
#          for counter in range(0,10):
#               body of for loop

# for i in range(5,0,-1):
#     print("* "*(i))
#

# While Loop:
#   counter = 0
#   while counter<=10:
#       body of while loop
#       increament/dec

# counter = 0
# while counter <10:
#     print(counter)
#     counter +=1
n = 6
for i in range(1,n):
    print(" "*(n-i),end="")
    print("* "*i)


#      *
#     * *
#    * * *
#   * * * *
#  * * * * *
# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *