# wap program which will print positive and negative number,

n=int(input("enter value:"))
if(n==0):
    print("zero not valid")
else:
    print("numbers within in {}",n)
    i=1
    while(i<n):
        print("\t{}".format(i))
        i=i+1 #updation
    else:
        j=-1
        while(j>=n):
            print("\t{}".format(j))
            j=j-1
        else:
            print("*"*40)
