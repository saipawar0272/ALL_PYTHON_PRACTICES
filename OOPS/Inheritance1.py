
#Inheritance

#what can be inherited
#constructor
# non private Attribute
# non private method

#parent class

class user:
    def __init__(self):
        self.name='sai'

    def login(self):
        print('login')

#child class

class student(user):
    #def __init__(self):
     #   self.rollno=133
    def enroll(self):
        print("enroll into data  & eng batch")

u=user()
s=student()
print(s.name)

#constructor

