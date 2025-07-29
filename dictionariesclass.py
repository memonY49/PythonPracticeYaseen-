# Dictionaries:
#    A dict is a sequance or a collection of key and value pairs.

# mydict = {"Name":"Yasir",
#           "FName":"Nawaz",
#           "Phone":"030405000005",
#           "Cnic":4130484938493,
#           "Email":"abc@gmail.com",
#           "Pass":"abc123"}
#
# mydict["Add"] = "hbbhvsdjhvdhsdvb"
#
#
# print(mydict)
# print(len(mydict))
#
# Dict functions:
#       keys()
#       values()
#       items()

# print(list(mydict.items()))


data = {"user1":{"Name":"Yasir",
                "FName":"Nawaz",
                "Phone":"030405000005",
                "Cnic":4130484938493,
                "Email":"abc@gmail.com",
                "Pass":"abc123"},
        "user2":{"Name":"Yasir",
                "FName":"Nawaz",
                "Phone":"030405000005",
                "Cnic":4130484938493,
                "Email":"abc@gmail.com",
                "Pass":"abc123"},
        "user3":{"Name":"Yasir",
                "FName":"Nawaz",
                "Phone":"030405000005",
                "Cnic":4130484938493,
                "Email":"abc@gmail.com",
                "Pass":"abc123"},
        "user4":{"Name":"Yasir",
                "FName":"Nawaz",
                "Phone":"030405000005",
                "Cnic":4130484938493,
                "Email":"abc@gmail.com",
                "Pass":"abc123"}}

print(data["user3"]["Email"])