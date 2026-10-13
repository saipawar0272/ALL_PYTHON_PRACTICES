#program to  demonstrate class level example

class Employee:
    @classmethod
    def getcompdet(cls): #class level method
        cls.compname="WIPRO"
        Employee.city="HYD"
    @classmethod
    def dispcompdet(cls):
        cls.getcompdet() #calling cls level method w.r.t.cls
        print("comp name:{}".format(cls.compname))
        print("city name:{}".format(cls.city))
        print("-------------OR---------------")
        print("comp name:{}".format(Employee.compname))
        print("city name:{}".format(Employee.city))


#main program
Employee.getcompdet()
Employee.dispcompdet()

