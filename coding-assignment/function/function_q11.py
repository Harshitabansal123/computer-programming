#11. Find the Length of a String Without Using len()
#Write a function that returns the length of a string without using the built-in len() function.

def string_length(s):
    count = 0
    for char in s:
        count += 1
    return count
print(string_length("hello"))
