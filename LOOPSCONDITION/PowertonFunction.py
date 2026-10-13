#wap program for calculating x^n

def powerton():
    x=int(input("enter number:"))
    n=int(input("enter number:"))
    result=x**n
    return x,n,result

#main program

x,n,res=powerton()
print("power({},{})={}".format(x,n,res))