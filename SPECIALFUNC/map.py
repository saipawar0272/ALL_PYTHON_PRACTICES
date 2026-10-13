#program which will accept list of old salary and increment it by 20%

def increment(sal):
    sal=sal+sal*(20/100)
    return sal


#main program
print("enter list of old salaries:")
oldsal=[float(sal) for sal in input().split()]
print("list of old salaries=",oldsal)
nsl=map(increment,oldsal)  #here nsl is called an object of<class,map>
print(nsl,type(nsl))
#convert map object into list type
newsal=list(nsl)
print("new sal lit=",newsal)