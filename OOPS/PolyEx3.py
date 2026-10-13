#
class Circle:
    def __init__(self):
        self.r=float(input("Enter Radius:"))
        self.ac=3.14*self.r**2
        print("Area of Circle:{}".format(self.ac))

class Square:
    def __init__(self):
        self.s=float(input("Enter side:"))
        self.sa=self.s**2
        print("Area of Square:{}".format(self.sa))

class Rect:
    def __init__(self):
        self.l=float(input("Enter length:"))
        self.b=float(input("Enter Breadth:"))
        self.ra=self.l*self.b
        print("Area of Rect={}".format(self.ra))
        super().__init__()
        Circle.__init__(self)

#main program
r=Rect()  #object creation
