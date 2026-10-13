#program to deminstrate global keyword
def incr():
    global a
    a=a+1

def update():
        global a
        a=a*2

#main program
a=10 #here a is called global variable
print("val of a before increment{}".format(a))
incr()
print("val of b after increment{}".format(a))
update()
print("val of a after update{}".format(a))