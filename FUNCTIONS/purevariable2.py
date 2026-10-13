#program to demonstrate the pure variable
def disval(*a):
    print("*"*50)
    for v in a:
        print("{}".format(v),end="")
        print()


#main program
disval(10,20,30,40,50)
disval(10,20,30,40)
disval(10,20,30)
disval(10,20)
disval(10)