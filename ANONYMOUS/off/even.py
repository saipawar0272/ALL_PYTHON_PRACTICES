#wap program which will accept list of elements dynamically and filter them in even and odd

print("enter list of elements dynamically:")
lst=[int(x) for x in input().split()]
  #define filter for even and odd

e1=list(filter(lambda x:x%2==0,lst))
o1=list(filter(lambda y:y%2!=0,lst))

print("original elements={}".format(lst))
print("even elements ={}".format(e1))
print("odd elements={}".format(o1))
