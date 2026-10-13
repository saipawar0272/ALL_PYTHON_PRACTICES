
#reading from file

f = open('sample.txt')
data=f.read()

print(data)
print("*"*45)

data2=f.read(10)
print(data2)
f.close()

print("*"*45)
