#program for understanding how to create sub threads

import threading
from time import thread_time_ns


def welcome(name1):
    print("{}----->hi {}, good evening".format(threading.current_thread().name,name1))

#main program
print("program execution started:{}".format(threading.current_thread().name))
#create sub threads
t1=threading.Thread(target=welcome,args=("sai",))

#assign user friendly name to sub threads

t1.name="ganesh"   #t1.setName("ganesh")  here setName()  is Deprecated on the name of "name" attribute
t1.start()
print("Program execution ended:{}".format(threading.current_thread().name))