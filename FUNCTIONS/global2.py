#program to demonstrate global()

a=10
b=20
c=30
d=40
 #here a,b,c,d are called global variable

def operation():
     a=100
     b=200
     c=300
     d=400 #here x,y,z are called local variable
     res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
     print("sum=",res)

#main program
operation()

