#program to check if the given string is a palindrome string or not
a=input("enter")
c = a[::-1]
if a==c:
    print("Palindrome")
else:
    print("Not a palindrome")
