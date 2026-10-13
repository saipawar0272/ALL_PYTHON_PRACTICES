#write python program which will validate mobile number by using regular expression

import re

while(True):
  mno=input("Enter mobile number:")
  if(len(mno)==10):
      res=re.search(r"\d{10}",mno)
      if(res!=None):
          print("\t{} is a valid mobile number".format(mno))
          break
      else:
          print("\t{} is a invalid mobile number because it contains non-int value--try again".format(mno))
  else:
    print("\t{} is invalid ".format(mno))



