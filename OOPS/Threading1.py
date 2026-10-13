
#program for finding demonstrating default thread

import threading
tname=threading.current_thread().name
print("Deafult thread name:{}".format(tname))
print("number of threads by defualt=",threading.active_count())