#program for cal div of two numbers handling all types of specific exceptions

try:
    print("program execution started")
    s1=input("enter first value:")
    s2=input("enter second value:")
    a=int(s1)
    b=int(s2)
    c=a/b
except (ZeroDivisionError,ValueError):  #multi -exception handling block
   print("\t DONT ENTER 0 FOR DENO")
   print("\t DONT ENTER ALNUMS,STRS AND SYMBOLS")

else:
    print("----else-----")
    print("fisrt value=",a)
    print("second value=",b)
    print("div=",c)
finally:
    print("\t program executed successfully")