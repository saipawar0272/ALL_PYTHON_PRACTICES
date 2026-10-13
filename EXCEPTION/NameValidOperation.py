from bdb import Breakpoint

from NameExcept import NameValidError,ZeroLengthError

def  validprocess(name):
  if(len(name)==0):
    raise ZeroLengthError
  else:
    words=name.split()
    valid=True
    for word in words:
        if(not word.isalpha()):
            valid=False
            break
    if(valid):
        return "{} is valid name".format(name)
    else:
        raise NameValidError

validprocess("sai pawar")