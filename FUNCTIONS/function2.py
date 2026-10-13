#define function for addition of two numbers
def addop(x,y):   #here x,y are called formal parameters
    z=x+y  #here z is called local variable
    return z
 #Main program
print("-"*50)
a=float(input("enter 1st value:"))
b=float(input("enter 2nd value:"))
res=addop(a,b)  #function call
print("({},{})={}".format(a,b,res))
print("-"*50)
x=float(input("Enter 1st number:"))
y=float(input("Enter 2nd number:"))
z=addop(x,y) #function call
print("sum({},{})={}".format(x,y,z))
print("+"*50)
