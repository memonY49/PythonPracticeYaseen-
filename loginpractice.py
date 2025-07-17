
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



Name = "Yasir"
FName = "Nawaz"
Cnic = "41305-33884444-1"
Phone = "0304-00000000"
Email = "abc@GMAIL.COM"
Pass = "ABC123"

userEmail = input("Enter your email:")      # Here I'm taking user email as an input



if userEmail == Email:
    userPass = input("Enter your password")
    if userPass == Pass:
        print("Name:", Name)
        print("FName:", FName)
        print("Cnic:", Cnic)
        print("Phone:", Phone)
        print("Email:", Email)
    else:
        print("Password is incorrect!")
else:
    print("Email is incorrect!")

