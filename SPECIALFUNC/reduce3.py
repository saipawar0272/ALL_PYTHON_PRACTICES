#pyton program which will accept list of words  and obtain single line of text by using reduce ()

import functools
print("Enter list of words seprated by comma:")
lst=[str(val) for val in input().split(",")]
res=functools.reduce(lambda k,v :k+" "+v,lst)
print("line of text")
print(res)

