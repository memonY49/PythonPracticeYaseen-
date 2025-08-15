#

# Infinite loop
#
#
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
#
# while True:
#     print("1.Add")
#     print("2.Sub")
#     print("3.Mul")
#     print("4.Div")
#     print("0.Exit")
#     try:
#         choice = int(input("Enter your selection: "))
#         if choice == 1:
#             v1 = int(input("Enter value 1: "))
#             v2 = int(input("Enter value 2: "))
#             print(f"Result: {add(v1, v2)}")
#         elif choice == 2:
#             v1 = int(input("Enter value 1: "))
#             v2 = int(input("Enter value 2: "))
#             print(f"Result: {sub(v1, v2)}")
#         elif choice == 3:
#             v1 = int(input("Enter value 1: "))
#             v2 = int(input("Enter value 2: "))
#             print(f"Result: {mul(v1, v2)}")
#         elif choice == 4:
#             v1 = int(input("Enter value 1: "))
#             v2 = int(input("Enter value 2: "))
#             print(f"Result: {div(v1, v2)}")
#         elif choice == 0:
#             break
#     except ValueError as ve:
#         print("Invalid Selection .....")


# Create a Never ending Car showroom application which contains a list of five companies and there should be
# five cars each. create a function to show manu of companies to the user when user selects any company
# call a function which show a  manu of five cars of that selected company. when user selects the car
# than call a function which shows all details of that selected car

data = [[{"Company":"Toyota","Name":"Corolla","Model":"GLI","Year":"2017","Price":0000},
         {"Company":"Toyota","Name":"Altus","Model":"1.6","Year":"2008","Price":0000},
         {"Company":"Toyota","Name":"Corolla","Model":"XLI","Year":"2005","Price":0000},
         {"Company":"Toyota","Name":"Land cruisor","Model":"2.0","Year":"2012","Price":0000},
         {"Company":"Toyota","Name":"Range Rover","Model":"1.8","Year":"2015","Price":0000}],
        [{"Company":"Suzuki","Name":"Mehran1","Model":"VXR","Year":"2008","Price":0000},
         {"Company":"Suzuki","Name":"Mehran2","Model":"VXR","Year":"2008","Price":0000},
         {"Company":"Suzuki","Name":"Mehran3","Model":"VXR","Year":"2008","Price":0000},
         {"Company":"Suzuki","Name":"Mehran4","Model":"VXR","Year":"2008","Price":0000},
         {"Company":"Suzuki","Name":"Mehran5","Model":"VXR","Year":"2008","Price":0000}]]
