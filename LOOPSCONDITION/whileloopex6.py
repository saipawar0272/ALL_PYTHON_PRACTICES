#program for odd numbers
n=int(input("Enter the number:"))
if(n%2!=0):
    print("odd number")
else:
    i=2
    while(i<=n):
        print("{}".format(i))
        i=i+2

