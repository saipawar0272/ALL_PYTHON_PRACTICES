#adding of two numbers using lambda function
def addop(a,b):  #normal function
    c=a+b
    return c

sumop = lambda a,b : a+b  #anonymous function
#main program
res=addop(10,45)
print("sum=",res)
print("type of addop=",type(addop))
print("*"*50)
x=sumop(200,56)  #anonymous function call
print(x,type(x))
print("type of sumop= ",type(sumop))

