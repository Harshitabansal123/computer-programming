#9. Remove All Non-Alphabetic Characters
#Problem: Remove all non-alphabetic characters from the string "hello123 world!@#".

s = "hello123 world!@#"
cleaned_s = ''.join(c for c in s if c.isalpha())
print(cleaned_s)
