#python program which will accept list of values from keyboard and find max and min by using anonymtious functtion  with list comprehension
findmax = lambda values: max(values)
findmin = lambda values: min(values)

#main program
print("Enter list of values seprated by space:")
vals=[int(val) for val in input().split()] #list comprehension
print("content of list=",vals)
bv=findmax(vals)  #anonymous function
sv=findmin(vals)
print("max({})={}".format(vals,bv))
print("min({})={}".format(vals,sv))