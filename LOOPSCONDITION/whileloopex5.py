#program to genrate even numbers
n=int(input("enter the even number:"))
if(n%2!=0):
    print("{} odd  numbers".format(n))
else:
    i=2
    while(i<=n):
        print("{}".format(i))
        i=i+2