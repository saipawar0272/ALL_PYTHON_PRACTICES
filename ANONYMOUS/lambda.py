#define lambda or anonymous functions for finding sum,sub and mul operations on two numbers

def sumop(a,b):
    c=a+b
    return c

addop=lambda x,y:x+y #anonymous function
subop=lambda a,b:a-b #anonymous function
mulop=lambda x,y:x*y #anonymous function

#main program
result=sumop(10,20)
print("sum of 2 numbers with normal function={}".format(result))

result1=addop(100,200)
print("add of 2 numbers={}".format(result1))
result2=subop(50,20)
print("sub of 2 numbers ={}".format(result2))
result2=mulop(56,2)
print("mul of 2 numbers ={}".format(result2))
