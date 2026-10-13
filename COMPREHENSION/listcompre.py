#python program which contain positive number from list of mixed numerical values;

print("Enter list of values seprated by comma:")
pslist=[float(val) for val in input().split(",") if float(val)>0]
pslist1=[float(val) for val in input().split(",") if float(val)<0]
print("print +val=",pslist,type(pslist))
print("list of -ve value=",pslist1)

