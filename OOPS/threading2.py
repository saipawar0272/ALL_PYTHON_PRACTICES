#program for demonstrating Main thread Executes all the functions one by one --Sequential Execution
import threading
def welcome():
      print("{}--welcoming to multithreading concepts".format(threading.current_thread().name))

def greet():
      print("line no 5:{}--Good Evening".format(threading.current_thread().name))
def hi():
      print("line no 8:{}--Good Afternoon".format(threading.current_thread().name))
#main program

print("Program execution started:{}".format(threading.current_thread().name)) #main thread
welcome()
print("line no -12")
greet()
print("line no --13")
hi()
print("program execution ended")
