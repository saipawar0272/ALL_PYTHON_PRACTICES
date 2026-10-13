#python program for demonstrating pure variable length arguments
def disval(*a): #here*a is called variable length parameter and whose type is tuple
 print(a,type(a))

disval(10,20,30,40,50) #function call-1 with 5 positional args
disval(10,20,30,40)
disval(10,20,30)
disval(10,20)
disval(10)