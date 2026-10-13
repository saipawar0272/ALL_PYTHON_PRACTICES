a=float(input("Enter first value:"))
b=float(input("Enter Second Value:"))
if(a>b):
    print(" ({},{})={}a is big".format(a,b,a))
else:
 if(b>a):
        print("({},{})={} b is big".format(a,b,b))
else:
    print("Both are equal")
