#program to filter positive and negative values from list

print("enter list of values sperated by space:\t\n")
lst=[int(val) for val in input().split()]
print("content of list=",lst)
#filter the +ve ans -ve values from lst
ps=list(filter(lambda val:val>0,lst))
ns=list(filter(lambda val:val<0,lst))
print("list of +ve values={}".format(ps))
print("list of negative values:{}".format(ns))