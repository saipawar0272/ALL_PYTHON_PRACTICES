#wap which performs te operations on local and global variable

a=10
b=20
c=30
d=40   #here a,b,c,d are called global variable

def operations():
    global c,d
    c=c+1 #val of c 31
    d=d+1 #val of d 41
    a=100
    b=200
    ga=globals()['a'] #ga=10
    gb=globals()['b'] #gb=20
    print("val of a (local)={}".format(a))
    print("val of b (local)={}".format(b))
    print("val of a(globl)={}".format(ga))
    print("val of b(global)={}".format(gb))
    result=c+d+a+b+ga+gb
    print("result={}".format(result))

#main program
operations()
