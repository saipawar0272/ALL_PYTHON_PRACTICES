#wap program which makes understand scope odf local and global

cap="INDIA" #global variable

def live():
    myplace="ts" #local
    print("{} is a part of {}".format(myplace,cap))

def live2():
    myplace='mumbai'
    print("{} us a part of {}".format(myplace,cap))

def live3():
    myplace='hyd'
    print("{} is a part of {}".format(myplace,cap))

live()
live2()
live3()