#program which will accept list of numerical values ans find sum of +ve numericao values and -ve numerical values

import functools
print("enter number sperated by comma:")
lst=[float(val) for val in input().split(",")]
posvals=list(filter(lambda val: val>0,lst))
negvals=list(filter(lambda val: val<0,lst))
print(posvals)
print(negvals)
psum=functools.reduce(lambda k,v: k+v,posvals)
nsum=functools.reduce(lambda k,v: k-v,negvals)
print("sum of +ve:({}+{})={}",psum)
print("sum of -ve:({}+{})={}",nsum)

