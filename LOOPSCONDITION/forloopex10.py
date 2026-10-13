#program to find factorial of number
n=int(input("enter the number:"))
if(n<0):
    print("{} invalid number")
else:
    f=1 #initialization multiplicative identtity
    for i in range(1,n+1):
        print("\t{}".format(i))
        f=f*i
    else:
        print("factorial({})={}".format(n,f,i))