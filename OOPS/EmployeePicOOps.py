from Employee import Emp
import pickle
class EmployeePic:
    def saveempdata(self):
        with open("emp.data","ab") as fp:
            #get employee data

             eno=int(input("enter number:"))
        ename=input("enter name:")
        sal=float(input("enter salary:"))
        print("*"*56)
    #create our own object
        eo=Emp()
        eo.getempdata(eno,ename,sal)
#save eo data to the file using pickle
        pickle.dump(eo,fp)
        print("Employee data saved successfully in file")
        print("*"*49)

#main program
EmployeePic().saveempdata() #calling instance method w.r.t name-less object