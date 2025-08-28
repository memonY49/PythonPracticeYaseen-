# file = open('data.txt','r')
# # file.write("yasir6,nawaz,03000000000,41999090939,abc@gmail.com,abc123\n")
# # print(file.readline())
# # print(file.readline())
# #
# # print(file.readlines())
# # for line in file.readlines():
# #     print(line.strip().split(',')[0])
#
# data = [line.strip().split(',') for line in file.readlines()]
#
# print(data)
#
#
# file.close()

# with open('data.txt','r') as file:
#     print([lin.strip().split(',') for lin in file.readlines()])


# print(file.read())


# data = []
#
# with open("data.txt",'r') as file:
#     data = [line.strip().split(',') for line in file.readlines()]
#
#
# userEmail = input("Enter your email:")
# userPass = input("Enter your password")
# for user in data:
#     if userEmail == user[4]:
#
#         if userPass == user[5]:
#             print("Name:", user[0])
#             print("FName:", user[1])
#             print("Cnic:", user[3])
#             print("Phone:", user[2])
#             print("Email:", user[4])
#             break
#         else:
#             print("Password is incorrect!")
#             break
# else:
#     print("Email is incorrect!")


# mode: a+,r+,w+

with open("data2.txt",'a+') as file:
    file.seek(0)
    # print(file.read())
    file.write('Yasir6,nawaz,03000000000,41999090939,abc5@gmail.com,abc123\n')









