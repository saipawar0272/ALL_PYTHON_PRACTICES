#wap to define biggest among two numbers

bigop=lambda a,b:a if (a>b) else b

#main program

x=float(input("enter  number:"))
y=float(input("enter second number:"))
print("big ({},{})={}".format(x,y,bigop(x,y)))