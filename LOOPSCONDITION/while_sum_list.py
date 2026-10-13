#wap program which will find the sum of the list

lst=[56,7,265,26,64,65,45,56]
s=0
i=0
print("Elements of list:")
while(i<len(lst)):
    print("\t{}".format(lst[i]))
    s=s+lst[i]
    i=i+1
else:
    print("sum={}".format(s))
