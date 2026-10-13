from ATMExcept import InSuffFundError
from ATMMenu import menu
from ATMOperations import deposit,withdraw,balenq
from ATMExcept import DepositError,WithdrawError,InSuffFundError
while(True):
  try:
    menu()
    ch=int(input("Enter your choice:"))
    match(ch):
      case 1:
        try:
           deposit()
        except ValueError:
            print("\t Don't Enter alnum and special characters")
        except DepositError:
            print("\t don't deposit zero values")
      case 2:
        try:
            withdraw()
        except ValueError:
            print("\t Don't Enter alnum and special characters")
        except WithdrawError:
            print("\t don; enter exceeded amount")
        except InSuffFundError:
            print("\t entered amount more than present amount")

      case 3:
          balenq()
      case 4:
          print("thnx for using programs")
          break

  except ValueError:
      print("Don't Enter alnums,strs and symbol for ur choice")

