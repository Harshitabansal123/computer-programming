#16. Find All Unique Pairs in a List
#Find all pairs in the list [1, 2, 3, 4, 5] whose sum is 5.

lst = [1, 2, 3, 4, 5]
target = 5
pairs = []
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.append((lst[i], lst[j]))
print(pairs)
