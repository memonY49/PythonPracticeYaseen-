
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

"""
This program is for the practice
in python programming language
"""





data = [["Yasir","Nawaz","41300736386","0304355570","abc@gmail.com","abc123"],
        ["Yasir","Nawaz","41300736386","0304355570","abc@gmail.com","abc123"],
        ["Yasir","Nawaz","41300736386","0304355570","abc@gmail.com","abc123"],
        ["Yasir","Nawaz","41300736386","0304355570","abc@gmail.com","abc123"],
        ["Yasir","Nawaz","41300736386","0304355570","abc@gmail.com","abc123"]]

userEmail = input("Enter your email:")
userPass = input("Enter your password")
if userEmail == data[4]:

    if userPass == data[5]:
        print("Name:", data[0])
        print("FName:", data[1])
        print("Cnic:", data[2])
        print("Phone:", data[3])
        print("Email:", data[4])
    else:
        print("Password is incorrect!")
else:
    print("Email is incorrect!")


mlist = [1,1,4,5,6,4]
