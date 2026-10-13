#program for finding cube of n natural numbers
n=int(input("enter number:"))
if(n<=0):
    print("{}invalid number".format(n))
else:
    s=0
    ss=0
    cs=0
    for i in range(1,n+1):
        print("\t{}\t\t{}\t\t{}".format(i,i*i,i*i*i))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("\t{}\t\t{}\t\t{}".format(s,ss,cs))