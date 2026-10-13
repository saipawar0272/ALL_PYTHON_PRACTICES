from ctypes import HRESULT


def powerton():
    x=int(input("enter first value:"))
    n=int(input("enter second value:"))
    result=x**n
    return x,n,result

#main program
x,n,result=powerton()
print("power ({},{})={}".format(x,n,result))