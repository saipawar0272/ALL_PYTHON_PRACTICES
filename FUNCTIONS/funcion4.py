# define function for addition of two numbers
#input: Taking from function call
#process: Taken place in function body
#output: Display inside of function body
def addop(a,b):
    #process
    c=a+b
    #result
    print("sum({},{})={}".format(a,b,c))
#main program
a=float(input("Enter 1st number:"))
b=float(input("enter 2nd number:"))
addop(a,b) #function call