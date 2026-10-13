#program to demonstrate global keyword
def modify1():
    global a,b
    a=a+1
    b=b+1

def modify2():
    global a,b
    a=a*2
    b=b*3

#main program
a,b=10,20
print("value of a,b before modifya={} b={}".format(a,b))
modify1()
print("value of a,b after modify a={} b={}".format(a,b))
modify2()
print("value of a,b after modify a={} b={}".format(a,b,a*b))

