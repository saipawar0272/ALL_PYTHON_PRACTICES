from multableexcept import NegNumError,ZeroError


def table(num): #here the value num is str,which is received from main program
  n=int(num)  # here implicitly there Possibility of raising error

  if(n<0):
      raise NegNumError
  elif(n==0):
      raise ZeroError
  else:
      print("mul table for :{}".format(n))

      for i in range(1,11):
          print("\t{}*{}".format(n,i,n*i))
          print("*"*50)

