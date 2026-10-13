class Customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address


class Address:

    def __init__(self,city,state,country):
        self.city = city
        self.country = country
        self.state = state


add1 = Address('Kathmandu','Bagmati','nepal')
add2 = Address('mumbai','Maharashtra','India')


cust1=('Shyam','Male',add1)
cust2=('Ganesh','Male',add2)

