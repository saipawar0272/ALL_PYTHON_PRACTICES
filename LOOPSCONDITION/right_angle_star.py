#format of right angle traingle

n=int(input("enter number:"))
if(n<=0):
    print("invalid number:")
else:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()

if(n<=0):
    print("invalid number:")
else:
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print()