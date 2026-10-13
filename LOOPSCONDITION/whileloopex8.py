#program to generate odd numbers in decreasing order
n=int(input("enter the number:"))
if(n<=0):
    print("invalid number {}".format(n))
else:
    print("print even numbers within {} to 2".format(n))
    n= n if(n%2!=0) else n-1
    while(n>=2):
        print("{}".format(n))
        n=n-2
    else:
        print("other statement")