#program to deteremine which will accept list of numerical values ans fnd their by sum using reduce functions

import functools
lst=[10,20,30,40,50]
res=functools.reduce(lambda k,v:k+v,lst)
print("sum=",res)
