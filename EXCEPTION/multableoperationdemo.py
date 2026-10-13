#main program
from multableoperation import table
from multableexcept import NegNumError
from multableexcept import ZeroError
while(True):
   try:
       n=input("Enter number for generating mul table:")
       table(n) #function call
   except ValueError:
       print("\tDon't Enter alnum,strs,special characters")
   except NegNumError:
       print("Don't enter Negative number")
   except ZeroError:
       print("Don't enter zero")
   else:
       print("thanx for using program")
       break