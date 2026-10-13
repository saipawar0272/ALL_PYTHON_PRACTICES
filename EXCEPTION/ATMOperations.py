

from ATMExcept import DepositError,WithdrawError,InSuffFundError
bal=500.00   #global variable
def deposit():
  damt=float(input("enter youe ammount:")) # implicitly error raises when value is alnum
  if(damt<=0):
      raise DepositError
  else:
      global bal
      bal=bal+damt
      print("Ur Account xxxxxxx1566 Credited with INR:{}".format(damt))
      print("now ur Account XXXXX1566 Bal INR:{}".format(bal))



def withdraw():
   wamt=float(input("enter ur withdraw amount"))
   global bal
   if(wamt<=0):
       raise WithdrawError
   elif(wamt>bal):
       raise InSuffFundError
   else:
       bal=bal-wamt
       print("ur Account xxxxxx1566 Debited With INR:{}".format(wamt))
       print("now ur Account xxxxxx1566 Bal INR:{}".format(bal))







def balenq():
    print("ur Account xxxxxx1566 bal INR:{}".format(bal))



