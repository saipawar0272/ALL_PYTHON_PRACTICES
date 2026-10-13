#function for addition of two numbers
#input:
#process:
#output:

def addop():
    #taking input
    a=float(input("Enter 1st number:"))
    b=float(input("enter 2nd number:"))
    #process
    c=a+b
    #return the value
    return a,b,c #return stmt can return one or more number of values
#main program
x,y,res=addop() #function call with multiline assignment
print("sum({},{})={}".format(x,y,res))
print("+"*50)
hyd=addop()  #function call with single line assignment
#hyd is an example of class tuple
print("sum({},{})={}".format(hyd[0],hyd[1],hyd[2]))
print("+"*50)
print("sum({},{})={}".format(hyd[-3],hyd[-2],hyd[-1]))
