#program to determine whether the given number is prime or not
n=int(input("ente the number:"))
if(n<=1):
    print("{} is invalid number".format(n))
else:
    res=False
    for i in range(2,n):
        if(n%i==0):
            res=True
            break
            if(res):
                print("{} is not prime".format(n))
            else:
                print("{] is prime".format(n))