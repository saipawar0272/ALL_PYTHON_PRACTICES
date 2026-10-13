#Finally

try:
    f = open('sample.txt','r')
except FileNotFoundError as e:
    print(e.args)
except Exception as e:
    print(e.args)
else:
    print(f.read())
finally:
    print('Always Finally block execute')