#this program obtains current thread in python environment

import threading
t=threading.current_thread()
t.join()
print(t)