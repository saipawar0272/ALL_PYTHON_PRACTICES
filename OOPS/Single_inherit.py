#single Inheritance

class phone:
    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying phone")

class SmartPhone(phone):
    pass

s = SmartPhone(25000,'apple',16).buy()