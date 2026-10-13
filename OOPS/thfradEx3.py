#pythton program which will display odd numbers separately and even numbers separately by using multiple threads

import threading,time
def odd(n):
    if(n<=0):
        print("{}----{} invalid input".format(threading.current_thread().name,n))
    else:
        for val in range(1,n+1,2):
            print("{}---odd value:{}".format(threading.current_thread().name,val))
            time.sleep(1)


def even(n):
    if(n<=0):
        print("{}-----{} invalid input".format(threading.current_thread().name,n))
    else:
        for val in range(2,n+1,2):
            print("{}----even Value:{}".format(threading.current_thread().name,val))
            time.sleep(1)


#main program
#create sub thread for operating odd numbers
t1=threading.Thread(target=odd,args=(10,))
#create sub thread for generating even numbers
t2=threading.Thread(target=even,args=(10,))
t1.start()
t2.start()


