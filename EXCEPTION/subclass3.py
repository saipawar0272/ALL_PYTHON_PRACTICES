#Div operations demo

from subclass import ZeroError
from subclass2 import divop
try:
    a=int(inout("enter number:"))
    b=int(input("Enter number:"))
    try:
        res=divop(a,b)  #function call either gives result or Exception
    except ZeroError:
        print("\t Don't Enter Zero for Deno")
    else:
        print("Div({}/{})={}".format(a,b,res))
    finally:
        print("i am from finally block")
except ValueError:
    print("\t Don't Enters alnum,strs and symbols")
finally:
    print("i am from outer finally block")