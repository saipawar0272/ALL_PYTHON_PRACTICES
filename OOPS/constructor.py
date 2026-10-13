
#constructor

class phone:
    def __init__(self,brand,price,camera):
        self.brand = brand
        self.price = price
        self.camera = camera

    def buy(self):
        print("buying phone")

class smartPhone(phone):
    def __init__(self,os,ram):
        self.os = os
        self.ram = ram
        print("inside smartphone constructor")

s = smartPhone("apple",35000)
print(s.os)
print(s.ram)
s.buy()


