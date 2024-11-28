#20. Remove All Elements Larger Than a Given Value
#Problem: From the list [1, 5, 2, 7, 3, 8, 4], remove all elements that are larger than 4.

lst = [1, 5, 2, 7, 3, 8, 4]
result = [item for item in lst if item <= 4]
print(result)
