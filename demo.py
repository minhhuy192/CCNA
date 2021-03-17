# caulater
# menu
print("**********MENU********")
print("1. sum", "2. sub", "3. multi", "4. dive")

option = int(input("input your option: "))

if (option == 1):
    a = int(input("input number 1: "))
    b = int(input("input number 2: "))
    print("{} + {} = {}".format(a,b,a+b))

elif (option == 2):
    a = int(input("input number 1: "))
    b = int(input("input number 2: "))
    print("{} + {} = {}".format(a,b,a-b))

elif (option == 3):
    a = int(input("input number 1: "))
    b = int(input("input number 2: "))
    print("{} + {} = {}".format(a,b,a*b))

elif (option == 4):
    a = int(input("input number 1: "))
    b = int(input("input number 2: "))
    print("{} + {} = {}".format(a,b,a/b))