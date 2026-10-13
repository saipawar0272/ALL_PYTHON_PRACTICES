#wap program which will content 2 list categories with map()

lst1=[23,45,67,23,90]
lst2=[34,56,78]

sumlist=list(map(lambda x,y:x+y,lst1,lst2))
print("list of elements={}".format(lst1))
print("list of elments={}".format(lst2))
print("*"*12)
print("sum of elements={}".format(sumlist))