#Problem: Remove Duplicate Elements from a Tuple
def remove_duplicates(tpl):
    return tuple(sorted(set(tpl)))

# Test case
tpl = (1, 2, 2, 3, 3, 4)
print(remove_duplicates(tpl))  # Output: (1, 2, 3, 4)
