#program to demonstrate local and global variable
lang="C++"
def learnAI():
    sub1="AI" #local variable

    print("{} ,{}".format(sub1,lang))

def learnML():
    sub2="ML" #local
    print("{},{}".format(sub2,lang))

learnAI()
learnML()