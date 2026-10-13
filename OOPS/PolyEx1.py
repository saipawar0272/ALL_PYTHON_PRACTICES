#PolyEx1.py

class Circle:
    def draw(self):
        print("Drawing circle:")

class Rect(Circle):
    def draw(self):
        print("Drawing Rect:")
        super().draw()

class Square(Rect):
    def draw(self): #overridden method
        print("Drwaing Square")
        super().draw()


#main program


so=Square()
so.draw()