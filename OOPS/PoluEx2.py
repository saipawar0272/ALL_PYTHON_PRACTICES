class Circle:
    def area1(self):  #original method
        self.r=float(input("Enter radius:"))
        self.ac=3.14*self.r**2
        print("Area of circle:{}".format(self.ac))

class Square(Circle):
    def area2(self): #overridden method
        self.s=float(input("Enter side:"))
        self.sa=self.s**2
        print("Area of Square:{}".format(self.sa))

class Rect(Square):
    def area(self):
        self.l=float(input("Enter length:"))
        self.b=float(input("enter breadth:"))
        self.ra=self.l*self.b
        print("Area of Rect={}".format(self.ra))
        Circle.area1(self)  #Class Name Approach
        Square.area2(self)  
        Rect.area(self)
#main program

r=Rect()
r.area()