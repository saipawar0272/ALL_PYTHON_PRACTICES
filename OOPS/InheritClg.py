#python program which will implement the following problem
#let us assume there exist university which contains university name and location
#accept university details
#let us assume there exist college which contains college name and its location,accept and display college details along with university details
#let us assume there exist college in which there exist student numbers,name, branch
#accept and display student details along with college and university details.

class Univ:
    def getUnivDet(self):
        self.uname=input("Enter university name:")
        self.uloc=input("Enter university location:")
    def disUnivDet(self):
        print("\tUniversity Name:{}".format(self.uname))
        print("\tUniversity clg:{}".format(self.uloc))
class College(Univ):
    def getCollDet(self):
        self.cname=input("Enter university Name:")
        self.cloc=input("Enter college location:")
    def dispCollDet(self):
        print("\tUniversity Name:{}".format(self.cname))
        print("\tUniversity location:{}".format(self.cloc))
class Student(College):
    def getStudDet(self):
        self.sno=int(input("Enter number:"))
        self.sname=input("enter name:")
        self.branch=input("Enter Student Branch:")

    def dispStudDet(self):
        print("\t Student Number:{}".format(self.sno))
        print("\t Student Name:{}".format(self.sname))
        print("\t Student branch:{}".format(self.branch))

#main program
so=Student()
so.getStudDet()
so.getCollDet()
so.getUnivDet()
so.disUnivDet()
so.dispCollDet()
so.dispStudDet()
