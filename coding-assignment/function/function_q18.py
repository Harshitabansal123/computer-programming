#18. Find the First Non-Repeating Character
#Write a function that returns the first non-repeating character in a string.

def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None
print(first_non_repeating("swiss"))
