#program for computing squares and cubes of list  of numbers by single default thread
import threading,time
def squares(lst):
    for val in lst:
        print("{}--squares({})={}".format(threading.current_thread().name,val,val**2))
        time.sleep(1)



#main program
print("program execution started")
lst=[2,4,26,56,1,16,48,9,48]
squares(lst)