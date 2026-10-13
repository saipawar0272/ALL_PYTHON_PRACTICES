#program to decide whether the number is prime or not
n=int(input("Enter a number to decide number prime or not:"))
if(n<=1):
    print("{} is invalid input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("{} is {}".format(n,res))

