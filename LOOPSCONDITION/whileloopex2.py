#program using if statement
n=int(input("enter the number you want:"))
if(n<=0):
    print("{}. is invalid input".format(n))
else:
    i=1
    while(i<=n):
        print("{}".format(i))
        i=i+1
    else:
        print("other block of statement")
