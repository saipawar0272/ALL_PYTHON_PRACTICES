
#use of with clause close the file automatically even if error occurs
#also ist is called as context manager

with open('sample.txt','r') as f:
    print(f.read())
    print(f.read())