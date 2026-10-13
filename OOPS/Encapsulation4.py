
class person:
    def __init__(self,name,country):
        self.name = name
        self.country = country

    def greet(self):
        if self.country == 'india':
            print("Namaste",self.name)
        else:
            print("hello",self.name)


p = person('Rahul','india')
print(p.country)
print(p.name)
p.greet()





