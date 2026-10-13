#wap to check given word palindrome

s=input("enter slice:")

if s == s[::-1]:
    print("palindrome")
else:
    print("not palindrome")