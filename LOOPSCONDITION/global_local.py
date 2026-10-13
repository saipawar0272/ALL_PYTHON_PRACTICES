
#wap which will specify use of global and local

a=10
b=20
c=30
d=40 #here a,b,c,d are called global variables

def operations():
    a=1
    b=2
    c=3
    d=4 #here a,b,c,d are called local variables

    ga=globals()['a']
    gb=globals()['b']
    gc=globals()['c']
    gd=globals()['d']
    localresult=a+b+c+d+ga+gb+gc+gd
    print("result=",localresult)

#main program
operations()
