#wap program

def sumop(a,b): #normal function def
    c=a+b
    return c

addop=lambda a,b:a+b #anonymous function
subop=lambda x,y:x-y #anonuymous function
mulop=lambda x,v:x*v #anonymous functions

result=sumop(10,60)
print("sum of two numbers={}".format(result))

result2=addop(50,90)
print("sum of 2 numbers ={}".format(result2))

print("sum of 2 numbers={}".format(addop(10,30)))
print("sub of 2 numbers={}".format(subop(50,25)))
print("mul of 2 numbers={}".format(mulop(20,10)))






