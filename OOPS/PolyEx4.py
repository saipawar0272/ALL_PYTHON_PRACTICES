class Circle:
    def __init__(self,c):
        print("Drawing--{}".format(c))
class Square(Circle):
    def __init__(self,s):
        print("Drawing-{}".format(s))
class Rect(Square):
    def __init__(self,s=None):pass
    def area(self):
        print("Drawing--Rect")
        super().__init__("Square")
        Circle.__init__(self,"Circle")

#main program
ro=Rect() #object Creation
ro.area()
#output
#drawing--square
#drawing--Rect