#17. Check for Anagram
#Write a function that checks if two strings are anagrams.

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
print(are_anagrams("listen", "silent"))
