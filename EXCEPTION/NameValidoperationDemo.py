
from NameValidOperation import validprocess
from NameExcept import NameValidError
name=input("enter ur Name:")

try:
    res=validprocess(name) #function call gives either result or exception
except NameValidError:
    print("{} invalid Name--try again".format(name))
except ZeroLengthError:
    print("name should not be empty")
else:
    print(res)