#16. Swap First and Last Character in a String
#Problem: Swap the first and last character in the string "hello".

s = "hello"
s = s[-1] + s[1:-1] + s[0]
print(s)
