n=int(input("Enter number:"))
if(n<=0):
    print("{} is invalid number:".format(n))
else:
    print("\tmultiplication table for:{}".format(n))
    i=1
    while(i<=10):
        print("\t{} * {}={}".format(n,i,n*i))
        i=i+1
    else:
        print("*"*40)
