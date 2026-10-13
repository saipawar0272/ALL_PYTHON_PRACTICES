a=int(input("Enter number:"))
b=int(input("Enter number:"))
print(a)
print(b)

a,b=b,a
print('swapped value of a:{}'.format(a))
print('swapped value of b:{}'.format(b))
print("{}>{}={}".format(a,b,a>b))