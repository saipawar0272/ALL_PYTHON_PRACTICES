#program to determine max and min value from list of numbers by using reduce function

import functools
print("Enter list of values seprated by space:")
lst=[float(val) for val in input().split()]
maxv=functools.reduce(lambda k,v: k if k>v else v,lst)
print("max({})={}".format(lst,maxv))

print("*"*50)
minv=functools.reduce(lambda k,v: k if k<v else v,lst)
print("min({})={}".format(lst,minv))

