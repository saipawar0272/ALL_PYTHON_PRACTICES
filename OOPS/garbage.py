
import gc

if(gc.isenabled()==True):
    print("gc is running",gc)


a=23
b=32
gc.disable()
c=a+b
print("c=",c)

print("gc is not running")


