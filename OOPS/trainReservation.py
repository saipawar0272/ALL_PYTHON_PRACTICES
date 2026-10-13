
import threading,time
def reservation(nos):
    L.acquire()
    global totnos
    if(nos>totnos):
       print("hi {},{}seats are not available try next time".format(threading.current_thread().name,nos))
       time.sleep(2)
    else:
       totnos=totnos-nos

       print("\t Hi {},{} Seats are reserved -happy journey".format(threading.current_thread().name,nos))
       time.sleep(2)
       print("\tNow available seats={}".format(totnos))
       time.sleep(2)
       if(totnos==0):
           print("\t Train is Full")
    L.release()




#main program
L=threading.Lock()
totnos=14 #total no of seats
#create number of subthreads--passengers

t1=threading.Thread(target=reservation,args=(22,))
t1.name="Asim"
t2=threading.Thread(target=reservation,args=(5,))
t2.name="sai"
t3=threading.Thread(target=reservation,args=(8,))
t3.name="ganesh"
t4=threading.Thread(target=reservation,args=(3,))
t4.name="soma"
t5=threading.Thread(target=reservation,args=(2,))
t5.name="sush"

#Dispatch the sub threads

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
