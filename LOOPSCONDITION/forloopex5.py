#program for multiplication of numbers using for
n=int(input("Enter number:"))
if(n<=0):
    print("invalid number{}".format(n))
else:
    for i in range(1,11):
        print("{}*{}={}".format(i,n,i*n))
