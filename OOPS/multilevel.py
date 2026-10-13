#multilevel inheritance

class product:
    def review(self):
        print("product customer review")

class phone(product):
    def __init__(self,price,brand,camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("buying phone")

class SmartPhone(phone):
    pass

class FuturePhone(phone):
    pass

s = SmartPhone(25000,'apple',16)
f = FuturePhone(74565,'samsung',12)
s.review()
s.buy()
f.buy()