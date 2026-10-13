#program to demonstrate global keyword

def modify1():
    global a,b
    a=a+1
    b=b+1

def getvals():
    #there is no need to write global keywords because we wre not modifying global variable but just we are accessing
    c=a*2
    d=b*3  #here c and d are called local variable
    print("inside of getvals()---> c={} d={}".format(c,d))

#main program
a,b=10,20  #here a,b are called global variable
print("in main program before modify a={} b={}".format(a,b))
modify1()
print("in main program after modify a={} b={}".format(a,b))
getvals()
print("in main program inside of getvals a={} b={}".format(a,b,a*b))