## wap which will accept 3 integer values and find biggest among them

a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))


if  a > b and a>c:
    print("a is greater={}".format(a))
elif b>c:
    print('b is greater={}'.format(b))
else:
    print("c is greater={}".format(c))

############################################

if(a==b) and (a==c):
    print("all values are equal")
else:
    big=a
    if(b>big):
        big=b
        if(c>big):
            big=c
            print("biggest of ({},{},{} is {})".format(a,b,c,big))