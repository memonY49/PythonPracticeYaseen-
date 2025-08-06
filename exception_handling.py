# exception : error
# There are two clauses in exception handling
# 1- try clause
# 2- except clause
# optional default clause
try:
    userin = int(input("Enter a number: "))
except Exception as e:
    print("Invailed input!!")
finally:
    print("....Thank You....")





