#program to cal to div and val error:
try:
  print("program execution starts")
s1=int(input("Enter number:"))
s2=int(input("Enter number:"))
a=int(s1)
b=int(s2)
c=a/b
except (ZeroDivisionError,valueError):
   print("\t DONT ENTER 0 FOR DENO")
   print("\t DONT enter alnum")
else:
   print("div=",c)
finally:
   print("peogram executed")