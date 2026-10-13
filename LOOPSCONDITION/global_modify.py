#wap program which will modify global variable in various function definition

a=10 #global variable
def modifyval():
    global a #refering global variable value
    a=a+1 #modifying global variable value
    print("val of a in modify val()={}".format(a))
def updateval():
    global a # refering global variable value
    a=a*2 #modifying global variable value
    print("val of a in update val()= {}".format(a))

#main program

print("val of a before modification by the functions={}".format(a))
modifyval()
print("val of a after modifyval()={}".format(a))
updateval()
print("val of a after update val ()={}".format(a))