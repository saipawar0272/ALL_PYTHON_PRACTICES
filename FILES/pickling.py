#program which will accept number of employee details,ename,esal,edetails and save using pickling concepts

import pickle
def saverecord():
    with open("emp.pic","ab") as fp:
    #get emp values from kbd:
              print("*"*40)
              eno=int(input("enter employee number:"))
              ename=input("enter employee name")
              sal=int(input("enter employee salary"))
              dsg=input("employee designation")

#create an empty list object
              lst=list()
              lst.append(eno)
              lst.append(ename)
              lst.append(sal)
              lst.append(dsg)
#save lst data into file
              pickle.dump(lst,fp)
              print("employee record saved in file successfully")
saverecord()