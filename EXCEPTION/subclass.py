#program which will handle zero division problems
a=input("Enter value:")
b=input("Enter value:")
from subclass2 import ZeroError
try:
  res=divop(a,b)   #function call-gives either result or exception
except ZeroError:
  print("\t Don't Enter Zero  for denom")
else:
  print("Div({}/{})={}".format(a,b,res))
finally:
 print("i am from else block")