#Program for finding Biggest of Two Numbers
from ctypes.wintypes import PSMALL_RECT

a=int(input("Enter Value of a:"))
b=int(input("Enter Value of B:"))
bc = a if b<a else a
print("Small({},{})={}".format(a,b,bc))