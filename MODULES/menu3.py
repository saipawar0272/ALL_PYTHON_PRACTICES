
#main program

from menu import menu
from menu import menu2
import sys
from menu2 import addop,subop,mulop,divop,modop,expop
while(True):
   menu()
ch=int(input("Enter your choice:"))
match(ch):
    case 1:addop()
    case 2:subop()
    case 3:mulop()
    case 4:divop()
    case 5:modop()
    case 6:expop()
    case 7:
        print("thnx for using program")
        sys.exit()

        print("ur selection is wrong")
