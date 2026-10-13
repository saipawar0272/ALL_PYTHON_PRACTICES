
import threading,time

def display(lst):
    for val in lst:
        print("{}---->{}".format(threading.current_thread().name,val))
        time.sleep(1)

#main program
#create sub thread
t1=threading.Thread(target=display,args=([4,45,75,1,549,41],))
print("Is sub thread running before start=",t1.is_alive())
#dispatch the sub thread
t1.start()
print("Is sub thread running after start=",t1.is_alive())
print("program execution ended")