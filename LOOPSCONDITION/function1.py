def addition(a,b):  #here a and b are called formal parameter
    c=a+b
    return c  #here c is called locqal

#main program
x1=int(input("enter number:"))
x2=int(input("enter number:"))
res1=addition(x1,x2) #function call
print("{}+{}={}".format(x1,x2,res1))