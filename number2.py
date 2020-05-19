str = input("Enter a string : ")
words = str.split()
lower = []
upper = []
for char in str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sortedstring = ''.join(lower+upper)
print(" \n arranging characters giving precedence to lowrecase")
print(sortedstring)