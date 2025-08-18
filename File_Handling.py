file = open('data.txt','r')
# file.write("yasir3,nawaz,03000000000,41999090939,abc@gmail.com,abc123\n")
# print(file.readlines())


for line in file.readlines():
    print(line.strip())





file.close()


