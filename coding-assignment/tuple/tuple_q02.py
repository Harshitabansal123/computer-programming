#Problem: Count Occurrences of an Element in a Tuple
def count_occurrences(tpl, element):
    return tpl.count(element)

tpl = (1, 2, 2, 3, 2, 4)
print(count_occurrences(tpl, 2))  # Output: 3
