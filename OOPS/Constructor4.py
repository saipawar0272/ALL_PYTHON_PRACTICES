
class Test:
    def __init__(self,a=1,b=2): #parameterized constructor
        self.a=1
        self.b=2
        print("val of a=",self.a)
        print("val of b=",self.b)

#main program
t1=Test() #object creation--PVM Calls default constructor
t2=Test(10,20)  #object creation--PVM calls parametrized constructor
t3=Test(b=2000,a=1316)