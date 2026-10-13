#program to demonstrate global
a=10
b=20   #here a,b are called global variables

def globalvarbs():
  a=100
  b=200   #here a,b are called local variable

print("*"*50)
print("invisible and programmer defined variables")
print("*"*50)
d=globals()
   for gvn,gvv in d.items():
      print("\t{}---->{}".format(gvn,gvv))
       print("*"*50)
print("programmer defined global variable")
print("*"*50)
print("global var-a=",d['a'])
print("global var-b=",d['b'])
print("*"*50)
#main program
getglobalvarbs() #function call