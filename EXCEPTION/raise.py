
class Bank:
    def __init__(self,balance):
        self.balance = balance

    def withdraw(self,amount):
        if amount < 0:
            raise Exception('Amount cannot be zero')
        if self.balance < amount:
            raise Exception('Insufficient Funds')

        self.balance = self.balance - amount


b = Bank(10000)
try:
    b.withdraw(2000)
except Exception as e:
    print(e.args)
else:
    print(b.balance)