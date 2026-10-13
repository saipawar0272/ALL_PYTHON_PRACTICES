#program for generating n to 1 numbers
n=int(input("Enter number:"))
if(n<=0):
    print("invalid number{}".format(n))
else:
    for i in range(n,0,-1):
        print("{}".format(i))