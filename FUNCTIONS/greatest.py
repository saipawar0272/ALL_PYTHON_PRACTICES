a=int(input("enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
big=a

if(b>big):
    big=b
    if(c>big):
        big=c
        print("biggest={}".format(big))
    else:
        print("biggest={}".format(big))
else:
    print("biggest={}".format(big))