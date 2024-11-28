#19. Find the Most Frequent Character in a String
#Problem: Find the most frequent character in the string "aabbbccccd".

from collections import Counter
s = "aabbbccccd"
count = Counter(s)
print(count.most_common(1)[0][0])
