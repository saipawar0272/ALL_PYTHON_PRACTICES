
#catching specific data


try:
    a= 10
    f = open('sample.txt','r')
    print(f.read())
    print(a)
    print(5/2)
    l = [1,2,3]
    l[5]
except FileNotFoundError as e: 
    print('In file not found except block')
except NameError as e:
    print('In variable not found block')
except ZeroDivisionError as e:
    print(e.args)
except Exception as e:
    print(e.args)


