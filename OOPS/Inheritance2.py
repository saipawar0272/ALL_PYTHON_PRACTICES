
#Inheritance

class A:
    def __init__(self):
        self.var = 100
    def display(self,var):
        print("inside a class",self.var)

class B(A):
    def display2(self):
        print("inside B class",self.var)


obj = B()
obj.display(200)