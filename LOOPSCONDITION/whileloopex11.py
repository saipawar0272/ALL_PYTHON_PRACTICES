#program for generating chars into words
word=input("enter word:")
print("given word={}".format(word))
i=0
while(i<len(word)):
  print("{}".format(word[i]))
i=i+1
i=len(word)-1
while(i>=0):
   print("\t{}".format(word[i])) 
