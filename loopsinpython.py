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
# n = 6
# for i in range(1,n):
#     print(" "*(n-i),end="")
#     print("* "*i)
#
# for i in range(n,0,-1):
#     print(" "*(n-i),end="")
#     print("* "*i)

# i = 1
# while i < n:
#     print(" "*(n-i),end = '')
#     print("* "*i)
#     i += 1
#
# i = n
# while i > 0:
#     print(" "*(n-i),end = '')
#     print("* "*i)
#     i -= 1

# Nasted loop:
#    loop inside a loop
#
# for i in range(0,5):
#     # body of outer loop
#     for j in range(0,3):
# #         body of inner loop
#         print(i,j)

# i = 0
# while i < 5:
#     j = 0
#     while j < 3:
#         print(i,j)
#         j += 1
#     i += 1


# For each loop:
# for loop works on any kind of sequances

data = [["Yasir","Nawaz","41300736386","0304355570","abc@gmail.com","abc123"],
        ["Yasir1","Nawaz","41300736386","0304355570","abc1@gmail.com","abc123"],
        ["Yasir2","Nawaz","41300736386","0304355570","abc2@gmail.com","abc123"],
        ["Yasir3","Nawaz","41300736386","0304355570","abc3@gmail.com","abc123"],
        ["Yasir4","Nawaz","41300736386","0304355570","abc4@gmail.com","abc123"]]

# for i in range(0,5):
#     print("Name:",data[i][0])

for user in data:
    print(user[0])




