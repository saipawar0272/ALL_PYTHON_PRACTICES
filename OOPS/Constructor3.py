#program to demonstrate default constructor

class Test:
    def __init__(self,a,b): # Parameterized constructor
        self.a=1
        self.b=2
        print("val of a=",self.a)
        print("val of b=",self.b)


#main program
t1=Test(10,20) #object creation--PVM calls parameterized constructor
t2=Test(100,200)
t3=Test(20,56)