#12. Find the Number of Words Starting with a Specific Letter
#Problem: Find how many words in the string "The quick brown fox" start with the letter "t".

s = "The quick brown fox"
print(len([word for word in s.split() if word.lower().startswith('t')]))
