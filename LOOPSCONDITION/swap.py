# wap which will swap the values without using third variable

a=int(input("enter number:"))
b=int(input("enter number:"))

print("original value of a",a)
print("original value of b",b)

a,b=b,a  #multiline assignment

print("swapped value of a",a)
print("swapped value of b",b)

print("a>b",a,b,a>b)
print('a is less than b',a,b,a<b)
print("a==b",a,b,a==b)
print('a<=b',a,b,a<=b)
print('a>=b',a,b,a>=b)
print('a!=b',a,b,a!=b)



