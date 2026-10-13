#python program which will accept list of numerical values and find thier square root

increment=lambda sal:sal+sal*20/100


#main function
print("enter list of old salaries:")
oldsals=[float(sal) for sal in input().split()]
nsl=map(increment,oldsals) #here nsl is called and object of <class,map>
#map object into list
newsal=list(nsl)
print("="*50)
print("old salary list\t\tNew salary list")
print("*"*50)
for osl,newsal in zip(oldsals,newsal):
    print("\t{}\t\t\t{}".format(osl,newsal))
    print("="*50)