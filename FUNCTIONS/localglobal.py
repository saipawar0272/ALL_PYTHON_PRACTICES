#program to demonstrate local and global variable
lang="python" #python global variable should alwyas be defined bfore function call or before the function definition
def learnAI():
    sub1="AI"
    print("to develope '{}' we use '{}' language".format(sub1,lang))

def learnML():
    sub2="ML"
    print("to develope '{}' language we use '{}' language".format(sub2,lang))


learnAI()
learnML()