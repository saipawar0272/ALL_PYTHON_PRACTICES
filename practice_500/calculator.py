#calculator

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    return x/y


print("please select option to perform")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.division")


while True:
    choice = input("Enter choice(1/2/3/4) : ")

    if choice in ('1','2','3','4'):

        try:
            num1 = int(input("Enter the number: "))
            num2 = int(input("Enter the number: "))
        except ValueError:
            print("invalid input.please enter number")
            continue

        if choice == '1' :
            print(num1, '+' , num2, '=', add(num1, num2))

        elif choice == '2' :
            print(num1, '-', num2 , '=', subtract(num1, num2))

        elif choice == '3' :
            print(num1, '*', num2, '=', multiply(num1, num2))

        elif choice == '4' :
            print(num1, '/', num2, '=', division(num1, num2))

        next_calculation = input("let's do next calculation? (yes/no)")
        if next_calculation == "no":
            break
    else:
        print('invalid input')

