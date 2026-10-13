#reloading modules
import shares
import time,importlib
def dispshares(d):
    print("SharesName\t\tSharesValue")
    print("*"*50)
    for sn,sv in d.items():
        print("\t{}\t\t{}".format(sn,sv))

#main program
d=shares.shareinfo()  #function call
dispshares(d)
time.sleep(15)
print("after coming out of 10 sec sleep:")
#Reloading the previously imported mofule -we use reload()--implib module depricated from imp module
importlib.reload(shares)
d=shares.shareinfo()  #function call
dispshares(d)