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

with open('data.txt','r') as file:
    print([lin.strip().split(',') for lin in file.readlines()])


print(file.read())