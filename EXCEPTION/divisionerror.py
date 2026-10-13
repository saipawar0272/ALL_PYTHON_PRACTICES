#program to cal div error

s1=input("Enter number")
s2=input("enter number")
a=int(s1)
b=int(s2)
c=a/b     #problematic statement--exception genrated stmt--zero division error
print("Div",c)
except ZeroDivisionError:
   print("\t Don't enter zero for deno....")
