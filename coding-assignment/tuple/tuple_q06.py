#Problem: Find the Index of an Element in a Tuple
def find_index(tpl, element):
    try:
        return tpl.index(element)
    except ValueError:
        return -1

tpl = (10, 20, 30, 40)
print(find_index(tpl, 30))  # Output: 2
print(find_index(tpl, 50))  # Output: -1
