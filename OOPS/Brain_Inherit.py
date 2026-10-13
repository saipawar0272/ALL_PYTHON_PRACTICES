#Aggregation (Has-A-relationship)


class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address


    def print_address(self):
        print(self.address.city,self.address.state,self.address.country)


class Address:
    def __init__(self,city,state,country):
        self.city = city
        self.state = state
        self.country = country




add1=Address('Mumbai','Maharashtra','India')
add2=Address('Hyderabad','Telangana','India')

cust1=Customer('Shyam','Male',add1)
cust2=Customer('Ramesh','Male',add2)

cust1.print_address()
cust2.print_address()



