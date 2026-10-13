#program for finding number of threads actively running by default

import threading
noact=threading.active_count()
print("number of active threads=",noact)
