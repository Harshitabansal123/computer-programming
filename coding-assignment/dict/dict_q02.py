#Program to find sum of all items in a Dictionary
dict = {'a': 100, 'b': 200, 'c': 300}
l = []
for i in dict:
    l.append(dict[i])
f = sum(l)
print("Sum :", f)
