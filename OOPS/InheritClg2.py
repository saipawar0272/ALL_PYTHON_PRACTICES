

from Univ import Univ
class College(Univ):
    def getCollDet(self):
        self.cname=input("Enter College Name:")
        self.cloc=input("Enter College location:")
    def dispCollDet(self):
        print("\tCollege Name:{}".format(self.cname))
        print("\tCollege location:{}".format(self.cloc))