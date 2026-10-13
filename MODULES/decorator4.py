#

def kvrlower(getln):
    def textconvert():
        line,us=getln()
        ls=line.lower()
        return line,us,ls
    return textconvert


def kvrupper(getln):
  def converttext():
      line=getln()
      us=line.upper()
      return line,us
  return converttext
@kvrlower
@kvrupper
def getlinetext():
    return input("Enter line of text:")

#main program
line,upr,lwr=getlinetext()
print("given line:",line)
print("upper text:",upr)
print("lower text:",lwr)
