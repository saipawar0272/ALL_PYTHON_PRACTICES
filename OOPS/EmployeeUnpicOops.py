from EmployeePicOOps import EmployeePic
import pickle
class EmployeeUnPic:
    def reademprecords(self):
        try:
            with open("emp.data","rb") as fp:
                
                record=pickle.load(fp)
                print(record.eno,record.ename,record.sal,type(record))

        except FileNotFoundError:
            print("file not exist")

#main program

EmployeeUnPic().reademprecords()