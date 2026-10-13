 #to demonstrate tuple comprehension
print("Enter list of values:")
val=int()
x=for val in input().split():
print("type of x=",type(x))

#convert generator object into tuple
tpl=tuple(x)
print("content of tpl=",tpl)
print("type of tpl=",type(tpl))

