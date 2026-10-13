
class BankAccount:
    def __init__(self):
        self.balance = 451356

    def __update_balance(self,amount):
        self.balance += amount

    def deposit(self,amount):
        self.__update_balance(amount)

acc = BankAccount()

print(acc.balance)
acc.deposit(5618)
print(acc.balance)




