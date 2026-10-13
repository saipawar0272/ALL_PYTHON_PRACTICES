#program for finding factorial of number using while
n=int(input("enter the number:"))
if(n<0):
    print("invalid number{}".format(n))
else:
    fact=1
    tn=n
    while(n>0):
        fact=fact*n
        n=n-1
    else:
        print("factorial({})={}".format(tn,fact))