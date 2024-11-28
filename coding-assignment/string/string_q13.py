#13. Find the Longest Prefix Matching a Substring
#Problem: Find the longest prefix of "abcdef" that is a substring of "abcdefghi".

s1 = "abcdef"
s2 = "abcdefghi"
prefix = ""
for i in range(min(len(s1), len(s2))):
    if s1[i] == s2[i]:
        prefix += s1[i]
    else:
        break
print(prefix)
