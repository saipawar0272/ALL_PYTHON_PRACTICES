#program for genrating mul table using oops

class MulTable:
    def getvalue(self):
        self.n=int(input("enter number:"))
    def gettable(self):
        self.getvalue()
        if(self.n<=0):
            print("{} is invalid number".format(self.n))
        else:
            print("*"*40)
            print("mul table for :{}".format(self.n))

            for i in range(1,11):
                print("\t{}*{}={}".format(self.n,i,self.n*i))

#main program

mt=MulTable()
mt.gettable()
