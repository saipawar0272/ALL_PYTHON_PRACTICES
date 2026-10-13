#program for generating n numbers up to 1
n=int(input("enter number:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    for i in range(1,n+1):
        print("\t{}".format(i))
