
#Method Overriding

#more than one method with same name and same parameter is called as overriding
#same method name with same parameter is called as method overriding
#same method name but different input parameter name is called as method overloading


class phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying a phone")

class SmartPhone(phone):

    def buy(self):
        print("buying a smartphone")

s=SmartPhone(25000,'apple',25)
s.buy()

