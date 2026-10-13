#program for adding of two numbers

class Sumop:
    def getvalues(self):
        so.a=float(input("enter first value:"))
        so.b=float(input("enter second value:"))
    def addvalues(self):
      self.c= self.a+self.b
    def dispvalues(kvr):
        print("first value={}".format(kvr.a))
        print("second value={}".format(kvr.b))
        print("sum of value={}".format(kvr.c))

#main program
so=Sumop() #object creation
print(so.__dict__)
so.getvalues()
print(so.__dict__)
so.addvalues()
print(so.__dict__)
so.dispvalues()
