#program for accepting digit and display number
# using dict data type
d=int(input("Enter any number:"))
d1={0:"Zer0",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
if(d1.get(d)==None):
    print("{} is number".format(d))
else:
    print("{} is {}".format(d,d1.get(d)))