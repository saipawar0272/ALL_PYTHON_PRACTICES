#thread program which will generate 1 to n numbers where n is positive

import threading,time

def generate(n):
    if(n<=0):
      print("{}----->{} is invalid input".format(threading.current_thread().name,n))
    else:
      print("------------------------")
      print("numbers within {}".format(n))
      for val in range(1,n+1):
          print("{}-----value:{}".format(threading.current_thread().name,val))
          time.sleep(1)
      else:
        print("-----------------")

#main program
t1=threading.Thread(target=generate,args=(10,))
t1.start()

