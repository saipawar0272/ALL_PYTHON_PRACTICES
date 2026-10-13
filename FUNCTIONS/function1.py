#define a function for addition of two numbers
def addop(a,b):   #here a,b are called formal parameters
    c=a+b #here c is called local variable
    return c
    #Main program
print("I am after the function definition")
res=addop(a=10,b=20) #function call
print("sum=",res)
print("----------------------")
res=addop(a=100,b=454)
print("sum=",res)