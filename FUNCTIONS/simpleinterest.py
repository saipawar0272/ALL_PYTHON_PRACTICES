#program to calculate simple interest and total amount to pay

p=float(input("Enter principle amount:"))
t=float(input("Enter time in months:"))
r=float(input("Enter rate of interest:"))

si=(p*t*r)/100
amountpay=p+si
print('{}'.format(amountpay))


print("*"*50)

#program which will display student details accepted from keyboard

sno=int(input("Enter student number:"))
sname=input("Enter student name:")
smarks=float(input("Enter student marks:"))
cname=input("Enter College name:")

print("print details")

print('{}'.format(sno))
print('{}'.format(sname))
print('{}'.format(smarks))
print('{}'.format(cname))