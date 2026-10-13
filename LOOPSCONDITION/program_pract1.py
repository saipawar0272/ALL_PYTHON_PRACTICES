from binascii import a2b_base64

#write python program which accept integer values and add them

a=float(input("enter number:"))
b=float(input("enter number:"))

print('value of a',format(a))
print('value of b',format(b))

c=a+b
print('value of c',format(c))


#wap which calculate simple interest and total amount to pay

p=float(input("enter principle amount:"))
t=float(input("time in months:"))
r=float(input("rate of interest:"))

c=p*t*r/100
d=c+p

print("principle amount=",p)
print('total time',t)
print('rate of interest',r)

print('total interest to pay=',format(c))
print("*"*50)
print('total amount with principle and interest=',d)











