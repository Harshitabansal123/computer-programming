#17. Find the Length of the Longest Substring Without Repeating Characters
#Problem: Find the length of the longest substring without repeating characters in "abcabcbb".

s = "abcabcbb"
max_len = 0
start = 0
char_index = {}
for end in range(len(s)):
    if s[end] in char_index:
        start = max(start, char_index[s[end]] + 1)
    char_index[s[end]] = end
    max_len = max(max_len, end - start + 1)
print(max_len)
