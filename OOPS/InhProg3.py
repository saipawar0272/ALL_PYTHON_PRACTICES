
#Inhprog3.py

class C1:
    def getA(self):
        self.a=100
class C2:
    def getB(self):
        self.b=200
class C3(C1,C2):
    def operation(self):
        self.c=self.a+self.b

#main program
o3=C3()
print(o3.__dict__)
o3.getA()
print(o3.__dict__)
o3.getB()
print(o3.__dict__)
o3.operation()
print(o3.__dict__)