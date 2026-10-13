#program by using set comprehension
print("Enter list of values seprated by space:")
val=int()
x={for val in input().split()}
print("content of st=",val,type(val))