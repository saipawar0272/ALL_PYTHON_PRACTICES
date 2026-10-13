#program for finding product of n natural numbers
n=int(input("enter number:"))
if(n<=0):
    print("{} invalid number".format(n))
else:
    s=1 #here s=1 called as multiplicative identity
    for i in range(1,n+1):
        print("{}".format(i))
        s=s*i
    else:
        print("product5 of {} numbers={}".format(n,s))
