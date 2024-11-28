#18. Find All Possible Substrings of a String
#Problem: Find all possible substrings of the string "abc".

s = "abc"
substrings = [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]
print(substrings)
