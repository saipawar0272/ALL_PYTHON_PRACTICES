
# swap two int values using xor

x=int(input("enter number:"))
y=int(input("enter number:"))

print("original value of x=",x)
print("original value of y=",y)

x=x^y
y=x^y
x=x^y

print('swapped value of x={}'.format(x))

print('swapped value of y={}'.format(y))