def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
print(" \n Please select operation:" \
      "1.Add\n"\
      "2.Subtract\n"\
      "3.Multiply\n"\
      "4.Divide\n")
s = int(input("Select operation from 1,2,3,4:"))
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if s == 1:
    print(a,"+",b,"=",add(a,b))
elif s == 2:
    print(a,"-",b,"=",subtract(a,b))
elif s == 3:
    print(a,"*",b,"=",multiply(a,b))
elif s == 4:
    print(a,"/",b,"=",divide(a,b))
else:
    print("Invalid input")
