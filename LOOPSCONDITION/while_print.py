#define a function for addition of two numbers


n=int(input("Enter a number:"))
if(n<=0):
    print("negative number:{}".format(n))
else:
    print("numbers with in :{}".format(n))
    i=1 #initialization part
    while(i<=n): #condition
        print("\t {}".format(i))
        i=i+1 #updation