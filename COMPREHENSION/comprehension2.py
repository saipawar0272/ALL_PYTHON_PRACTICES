#program to demonstrate reading values from keyboard
print("Enter list of values:")
val=int()
lst=[for val in input().split()]
print("Content of list=",lst)
print("type of lst=",type(lst))