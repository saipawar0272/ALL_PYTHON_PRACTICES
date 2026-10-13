
#super -->constructor

# we can't access super  keyword outside of the class

class phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera
        print("inside phone constructor")



class SmartPhone(phone):
    def __init__(self, price,brand,camera,os,ram):
        print("inside smartphone constructor")
        super().__init__(price,brand,camera)
        self.os = os
        self.ram = ram

s = SmartPhone(20000,'apple',20,'ios',16)
print(s.os)
print(s.price)



