#program to demonstrate reading values from keyboerd and find squares by using dict comprehension
print("enter list of values sperated by comma :")
d={int(val):int(val)**2 for val in input().split(",")}
print(d,type(d))
