#20.Find the Longest Substring with All Unique Characters
#Problem: Given a string "abcabcbb", find the length of the longest substring without repeating characters.

s = "abcabcbb"
n = len(s)

char_set = set()
left = 0
max_len = 0

for right in range(n):
    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    
    char_set.add(s[right])
    
    max_len = max(max_len, right - left + 1)

print(max_len)
