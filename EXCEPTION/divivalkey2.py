#program to use division default
#program developed by kvr on 08/08/025
#With forecasting knowledge of kvr , there is chance of modifying this code by programmer


try:
    print("program execution started")
    s1=input("enter number")
    s2=input("enter number")
    a=int(s1)
    b=int(s2)
    c=a/b
    s="PYTHON"
    print(s[10])
except ZeroDivisionError:
    print("\t Don't enter 0 for deno")
except ValueError:
    print("\t Don't enter alnum,strs")
except IndexError:
    print("Invalid index check index properly")
except:
    print("oops something is wrong")   #default except block used to handle unknown future exceptions

else:
    print("-------else-------")
    print("first value=",a)
    print("Second value=",b)
    print("Div=",c)
finally:
    print("program executed successfully")