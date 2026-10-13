#program for finding square of n natural numbers
n=int(input("enter number:"))
if(n<=0):
    print("{} is invalid number".format(n))
else:
    s=0
    ss=0
    for i in range(1,n+1):
        print("\t{}\t\t{}".format(i,i*i))
        s=s+i
        ss=ss+i**2
    else:
        print("\t{}\t\t\t{}".format(s,ss))