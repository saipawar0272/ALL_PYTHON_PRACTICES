# using dict type in three line
d=int(input("Enter Digit:"))
d1={0:"ZERO",1:"ONE",2:"TWO",3:"THREE",4:"FOUR",5:"FIVE",6:"SIX",7:"SEVEN",8:"EIGHT",9:"NINE"}
print("{} is {}".format(d,d1.get(d) if d1.get(d)!=None else "+ve number" if d1.get(d)==None else "-ve number"))