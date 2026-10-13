#program which will create folder

import os
try:
    os.mkdir("HYD\\python\\java")
    print("folder created")
except FileExistsError:
    print("folder already created")