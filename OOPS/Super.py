
#super keyword
#accesing parent class with child class using super keyword

class phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def sell(self):
        print("buying a phone")

class SmartPhone(phone):
    def buy(self):
        print("buying smartphone")
        #syntax to call parent method
        super().sell()

s=SmartPhone(25000,'apple',20)
s.buy()