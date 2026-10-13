
text = input("Enter text :").lower()

reversed_text =""

for i in text:
    reversed_text = i + reversed_text
    #print(reversed_text)
if  text == reversed_text:
        print("palindrome")
else:
        print("not palindrome")


