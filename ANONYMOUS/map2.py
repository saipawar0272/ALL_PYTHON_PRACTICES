#wap program which will accept list of integer values

print("enter values seprated with space:")

oldlst=[int (x) for x in input().split()]
sqlst=list(map(lambda x:x**2,oldlst))
print("old list={}".format(oldlst))
print("new lst={}".format(sqlst))