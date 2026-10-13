import re
gd="Python is an oop language.Python is also indenpendent language"
sd="thon"
res=re.search(sd,gd) #here res can be an object of <class ,re.match> or <class,none type>
if(res!=None):
    print("Search is successful")
else:
    print("search is unsuccessful")