#program for calculating factorial of number by using classes and object with constructor
class Factorial:
    def __init__(self,n):
        self.n=n
    def calfact(self):
        f=1
        if(self.n<0):
            print("{} is -ve number-no factorial".format(self.n))
        else:
            for i in range(1,self.n):
               f=f*i
            else:
                print("Factorial({})={}".format(self.n,f))

#main program
fo=Factorial(int(input("Enter number for cal factorial:"))) #object creation--calls paranetrized constructor
fo.calfact()
