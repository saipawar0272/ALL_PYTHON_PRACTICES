
text = input("Enter number :").lower()

if text == text[::-1]:
    print("palindrome")
else:
    print("not palindrome")