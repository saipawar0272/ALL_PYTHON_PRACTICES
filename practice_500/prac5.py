
#create menu method

class EmployeesManager:
    def __init__(self):
        self.employee=[]

    def menu(self):
        user_input =  input(""""
                               Enter your choice
                               1.press 1 to add employee
                               2.press 2 to display employee
                               3.press 3 to remove employee
                               4.Anything else to exist : """)

        if user_input == "1":
            self.add_employee()

        elif user_input == "2":
            self.display_employee()

        elif user_input == "3":
            self.remove_employee()

        else:
            exit()


    def add_employee(self):
        print("enter employee details :")
        name=input("enter name :")
        self.employee.append(name)
        age=input("enter age :")
        self.employee.append(age)
        salary=input("enter salary :")
        self.employee.append(salary)
        print("employee detail added successfully ")
        self.menu()


    def display_employee(self):
        if len(self.employee) == 0:
            print("no employee detail found")
            self.menu()
        else:
          for emp in self.employee:
            print(emp)

        self.menu()

    def remove_employee(self):
        for i in self.employee:
            print("deleting employees ")
            self.employee.remove(i)
        print("Removed specified employee ")

        self.menu()





obj=EmployeesManager()
obj.menu()
#obj.add_employee()


