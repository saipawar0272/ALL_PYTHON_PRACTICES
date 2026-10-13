#using anonymous lambda function
pos=lambda val: val>0
neg=lambda val: val<0

#main program
lst=[10,20,0,-45,-52,-12,70,82,54]
ps=filter(pos,lst)
ns=filter(neg,lst)
print("type of ps and ns",type(ps),type(ns))

#convert filter object into list object
pslst=list(ps)
#convert filter object into tuple object
nslst=tuple(ns)
print("Given list:{}".format(lst))
print("positive lst:{}".format(pslst))
print("negative lst:{}",format(nslst))