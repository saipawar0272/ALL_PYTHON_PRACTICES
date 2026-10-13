#program to demonstrate need of data encapsulation--data member

class Account:
    def getAccData(self): #instance method
        self.__acno=56
        self.__cname="ram"
        self.__bal=45899797
        self.__pin=4875
        self.bname="SBI"

#main program
ac=Account()
ac.getAccData()
print(ac.__dict__)