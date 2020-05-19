def prog(A):
    even = []
    odd = []
    for i in A:
        if(i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    print("Even lists:", even)
    print("Odd lists:", odd)
A = list()
n = int(input("enter size of the first list : "))
print("enter the elements of list: ")
for i in range(int(n)):
    k = int(input(""))
    A.append(k)
prog(A)