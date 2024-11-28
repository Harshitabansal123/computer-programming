#16. Find the Most Frequent Element in a List
#Write a function that finds the most frequent element in a list.

from collections import Counter
def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
print(most_frequent([1, 2, 2, 3, 3, 3, 4]))
