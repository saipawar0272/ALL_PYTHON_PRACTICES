#program for finding sum of n natural numbers
n=int(input("Enter the number:"))
if(n==0):
    print("{} is inavlid number:".format(n))
else:
    s=0 #initializing variable here s=0 called as additive identity
    for i in range(1,n+1):
        print("\t{}".format(i))
        s=s+i
    else:
        print("sum of {} numbers={}".format(n,s))
        
