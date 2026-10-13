#
from subclass import ZeroError
def divop(a,b):
   if(b==0):
       raise ZeroError  #here raise keyword is hitting or raising the programmer -defined exception
   else:
       return(a/b)

#phas 2: Defining the function with Business logic and hitting the Exception