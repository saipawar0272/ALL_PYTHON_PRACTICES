
#Class Relationship

#Aggregation
#Inheritance

#aggregation -- Has a Relationship

# to access private variable we need to write get  method

class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.show_city(),self.address.state,self.address.country)

class address:
    def __init__(self,city,state,country):
        self.__city = city
        self.state = state
        self.country = country

    def show_city(self):
        return self.__city



add1=address('mumbai','maharashtra','india')
cust1=customer('sai','male',add1)

cust1.print_address()




